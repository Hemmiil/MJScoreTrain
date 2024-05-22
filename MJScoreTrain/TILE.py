class tile():
    def __init__(self, rate=0.8):
        self.n = ""
        self.tiles = {}
        self.win_tile = {}
        self.rate = rate

    def KOOTSU(self):
        import random

        tiletype = random.choices(["man", "pin", "sou", "honors"], [9,9,9,7])[0]
        if tiletype == "honors":
            num = random.choices([f"{i}"*3 for i in range(1,8)])[0]
        else:
            num = random.choices([f"{i}"*3 for i in range(1,10)])[0]
        
        kootsu = {
            "type" : tiletype,
            "num" : num
        }

        return kootsu

    def SHUNTSU(self):
        import random

        tiletype = random.choices(["man", "pin", "sou"], [7,7,7])[0]
        num = random.choices([f"{i}{i+1}{i+2}" for i in range(1,8)])[0]
        shuntsu = {
            "type" : tiletype,
            "num" : num
        }
        return shuntsu

    def HEAD(self):
        import random

        tiletype = random.choices(["man", "pin", "sou", "honors"], [9,9,9,7])[0]
        if tiletype == "honors":
            num = random.choices([f"{i}"*2 for i in range(1,8)])[0]
        else:
            num = random.choices([f"{i}"*2 for i in range(1,10)])[0]
        
        head = {
            "type" : tiletype,
            "num" : num
        }

        return head
    
    def WIN(self):
        import random
        tiles = self.tiles
        length = [len(v) for v in tiles.values()]
        key = random.choices(list(tiles.keys()), length)[0]
        num = random.choices( [i for i in tiles[key]] )[0]
        return {key : num}

    def main(self):
        import random
        import numpy as np


        

        while True:
            tiles = {
                "man" : "",
                "pin" : "",
                "sou" : "",
                "honors" : ""
                    }       
            blocks = []
            warning = False
            blocks.append(self.HEAD())
            for i in range(4):
                blocks.append(random.choices([self.KOOTSU(), self.SHUNTSU()], [1-self.rate, self.rate])[0])

            for block in blocks:
                key = block["type"]
                num = block["num"]
                tiles[key] = f"{tiles[key]}{num}"
                tiles_key = [ i for i in tiles[key] ]
                tiles_key.sort()
                tiles[key] = "".join(tiles_key)
            
            for values in tiles.values():
                check = np.unique([i for i in values], return_counts=True)[1]
                if any(check>4):
                    warning = True
            
            if warning == False:
                break
            
        self.tiles = tiles

        self.win_tile = self.WIN() 
    

        return {"tiles" : self.tiles, "win_tiles" : self.win_tile}
        
        
