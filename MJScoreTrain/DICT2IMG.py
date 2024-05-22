class inp2img():
    def __init__(self):
        self.tiles = {}
        self.pathes = []
        self.win_path = {}

    def input(self, inp, win_tile):
        man = inp["man"]
        pin = inp["pin"]
        sou = inp["sou"]
        honors = inp["honors"]

        self.tiles = {
            "man" : man,
            "pin" : pin,
            "sou" : sou,
            "honors" : honors
        }
        self.win_tile = win_tile
        key = list(win_tile.keys())[0]
        tile = list(win_tile.values())[0]
        
        win_tile_in = self.tiles[key]
        
        for i in range(len(win_tile_in)):
            if win_tile_in[i] == tile:
                win_tile_in = win_tile_in[:i] + win_tile_in[i+1:]
                break
        
        self.tiles[key] = win_tile_in

    def inp2pathes(self):
        keys = ["man", "pin", "sou", "honors"]
        values = ["m", "p", "s", "j"]
        adict = {key : value for key, value in zip(keys, values)}
        pathes = []
        for key in keys:
            tiles = [ tile for tile in self.tiles[key].replace("0", "e")]
            for tile in tiles:
                path = f"./tile_imgs/0{adict[key]}{tile}.png"
                pathes.append(path)

        key = list(self.win_tile.keys())[0]
        tile = list(self.win_tile.values())[0].replace("0", "e")
        win_path = f"./tile_imgs/0{adict[key]}{tile}.png"
        
        
        self.pathes = pathes
        self.win_path = win_path

                   

    
    def path2img(self):
        from PIL import Image
        pathes = self.pathes
        imgs = []
        for path in pathes:
            img = Image.open(path)
            imgs.append(img)
        
        N = len(imgs)
        height, width = imgs[0].height, imgs[0].width

        dst = Image.new('RGB', ((N+2)*width, height))
        for i, img in enumerate(imgs):
            dst.paste(img, (i*width, 0))
        
        win_tile_img = Image.open(self.win_path)
        dst.paste(win_tile_img, ((N+1)*width, 0))
        return dst
    
    def main(self):
        self.inp2pathes()
        img = self.path2img()
        return img
        