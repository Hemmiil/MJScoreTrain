from mahjong.hand_calculating.hand import *
from mahjong.tile import *
from mahjong.hand_calculating.hand_config import *
from mahjong.meld import *
from mahjong.constants import *

import random

def HandCalculator_manual(inp_tiles, inp_win_tile, is_melds=False, is_tsumo=False, player_wind=SOUTH):

    calculator = HandCalculator()

    #アガリ形
    tiles = TilesConverter.string_to_136_array(man = inp_tiles["man"], 
                                               pin=inp_tiles["pin"], 
                                               sou=inp_tiles["sou"], 
                                               honors=inp_tiles["honors"], 
                                               has_aka_dora=False)

    #アガリ牌
    inp_win_tile_dict = {
        "man" : "",
        "pin" : "",
        "sou" : "",
        "honors" : ""
    }
    inp_win_tile_dict[list(inp_win_tile.keys())[0]] = list(inp_win_tile.values())[0]
    
    win_tile = TilesConverter.string_to_136_array(man = inp_win_tile_dict["man"],
                                                  pin = inp_win_tile_dict["pin"],
                                                  sou = inp_win_tile_dict["sou"],
                                                  honors = inp_win_tile_dict["honors"])[0]

    #鳴き

    if is_melds:
        melds = [
            #Meld(Meld.KAN, TilesConverter.string_to_136_array(man='2222'), False),
            Meld(Meld.PON, TilesConverter.string_to_136_array(man='333')),
            #Meld(Meld.CHI, TilesConverter.string_to_136_array(sou='567'))
            ]
    else:
        melds = None

    #オプション
    options = OptionalRules(
        has_open_tanyao = False,
        has_aka_dora = False,
        has_double_yakuman = True,
        # not implemented! tenhou does not support double yakuman for a single yaku
        kazoe_limit = HandConstants.KAZOE_LIMITED,
        kiriage = False,
        # if false, 1-20 hand will be possible
        fu_for_open_pinfu = True,
        # if true, pinfu tsumo will be disabled
        fu_for_pinfu_tsumo = False,
        renhou_as_yakuman = False,
        has_daisharin = False,
        has_daisharin_other_suits = False,
        has_daichisei = False,
        has_sashikomi_yakuman = False,
        limit_to_sextuple_yakuman = True,
        paarenchan_needs_yaku = True,
    )

    #アガリ方法、自風と場風
    def f(T_weight=1, F_weight=1):
        return random.choices([True, False], [T_weight, F_weight])[0]

    config = HandConfig(
            is_tsumo = is_tsumo,#f(1,4),
            is_riichi = True,
            is_ippatsu = False,
            is_rinshan = False,
            is_chankan = False,
            is_haitei = False,
            is_houtei = False,
            is_daburu_riichi = False,
            is_nagashi_mangan = False,
            is_tenhou = False,
            is_renhou = False,
            is_chiihou = False,
            is_open_riichi = False,
            player_wind = EAST,
            round_wind = player_wind,
            options=options
    )

    #ドラ
    dora_indicators = [
        TilesConverter.string_to_136_array(man='6')[0],#ドラ表示牌
        TilesConverter.string_to_136_array(pin='2')[0],
    ]



    result = calculator.estimate_hand_value(tiles, win_tile, melds=melds, dora_indicators=None, config=config,)

    return result

def main():
    import DICT2IMG
    import TILE
    import random
    import pickle
    import matplotlib.pyplot as plt
    from pandas import DataFrame
    from pandas import Series

    D = DICT2IMG.inp2img()
    T = TILE.tile(rate=0.9)
    T.rate = 0.9
    tiles = T.main()
    print("条件 : 全て立直、赤ドラあり、ドラは考慮しない")
    D.input(tiles["tiles"], tiles["win_tiles"])
    img = D.main()
    #plt.imshow(img)
    #plt.axis("off")

    is_tsumo = random.choices([True, False])[0]
    player_wind = random.choices([EAST, SOUTH, WEST, NORTH])[0]

    str_tsumo = {
        True : "ツモ",
        False : "ロン"
    }

    str_player_wind = {EAST : "親",
                SOUTH : "子 南家",
                WEST : "子 西家",
                NORTH : "子 北家"}

    plt.imshow(img)
    plt.axis("off")
    plt.show()
    print(str_tsumo[is_tsumo], str_player_wind[player_wind])

    ans_han = input("翻数を入力")
    ans_fu = input("符数を入力")
    ans_cost = input("点数を入力")

    result = HandCalculator_manual(inp_tiles=tiles["tiles"], inp_win_tile=tiles["win_tiles"], is_tsumo=is_tsumo, player_wind=player_wind)
    df = DataFrame({"翻数" : [ans_han, result.han],
                    "符数" : [ans_fu, result.fu],
                    "点数" : [ans_cost, result.cost["total"]]}, index=["回答", "正解"])
    display(df)


    print(result.yaku)



if __name__ == "__main__":
    main()




