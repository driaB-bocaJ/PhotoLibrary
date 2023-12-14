import random

from PIL import Image
from PIL.ImageDraw import ImageDraw
from kivy.app import App
from kivy.uix import image
from PIL import Image, ImageDraw
from kivy.uix.screenmanager import Screen


class PhotoEditApp(App):
    pass

class Display(Screen):
    def oldtimey(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r = 255 - pixels[x, y][0]
                g = 255 - pixels[x, y][1]
                b = 255 - pixels[x, y][2]
                sum = r + b + g
                avg = int(sum / 3)
                pixels[x, y] = (avg, avg, avg)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_blackandwhite.png")
        self.ids.pic.source = name + "_blackandwhite.png"
    def inverse(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r = 255 - pixels[x, y][0]
                g = 255 - pixels[x, y][1]
                b = 255 - pixels[x, y][2]
                red = (pixels[x, y][0] * 0) + r
                green = (pixels[x, y][1] * 0) + g
                blue = (pixels[x, y][2] * 0) + b
                pixels[x, y] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_inverse.png")
        self.ids.pic.source = name + "_inverse.png"
    def linedrawing(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        templist = []
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                templist.append(pixels[x, y])
            for z in range(len(templist)):
                if z > 0:
                    if (pixels[z, y][0] - templist[z - 1][0]) > 5:
                        red = pixels[z, y][0] * 0
                        green = pixels[z, y][1] * 0
                        blue = pixels[z, y][2] * 0
                    else:
                        maxred = 255 - pixels[z, y][0]
                        maxgreen = 255 - pixels[z, y][1]
                        maxblue = 255 - pixels[z, y][2]
                        red = pixels[z, y][0] + maxred
                        green = pixels[z, y][1] + maxgreen
                        blue = pixels[z, y][2] + maxblue
                    if (pixels[z, y][1] - templist[z - 1][1]) > 5:
                        red = pixels[z, y][0] * 0
                        green = pixels[z, y][1] * 0
                        blue = pixels[z, y][2] * 0
                    else:
                        maxred = 255 - pixels[z, y][0]
                        maxgreen = 255 - pixels[z, y][1]
                        maxblue = 255 - pixels[z, y][2]
                        red = pixels[z, y][0] + maxred
                        green = pixels[z, y][1] + maxgreen
                        blue = pixels[z, y][2] + maxblue
                    if (pixels[z, y][2] - templist[z - 1][2]) > 5:
                        red = pixels[z, y][0] * 0
                        green = pixels[z, y][1] * 0
                        blue = pixels[z, y][2] * 0
                    else:
                        maxred = 255 - pixels[z, y][0]
                        maxgreen = 255 - pixels[z, y][1]
                        maxblue = 255 - pixels[z, y][2]
                        red = pixels[z, y][0] + maxred
                        green = pixels[z, y][1] + maxgreen
                        blue = pixels[z, y][2] + maxblue
                    pixels[z, y] = (red, green, blue)
                else:
                    maxred = 255 - pixels[z, y][0]
                    maxgreen = 255 - pixels[z, y][1]
                    maxblue = 255 - pixels[z, y][2]
                    red = pixels[z, y][0] + maxred
                    green = pixels[z, y][1] + maxgreen
                    blue = pixels[z, y][2] + maxblue
                    pixels[z, y] = (red, green, blue)
            templist = []
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_linedrawing.png")
        self.ids.pic.source = name + "_linedrawing.png"
    def pointilism(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        canvas = Image.new(mode="RGB", size=(img.size[0], img.size[1]), color="white")
        for _y in range(100000):
            size = random.randint(5, 15)
            pix_x = random.randint(0, img.size[0] - size)
            pix_y = random.randint(0, img.size[1] - size)
            red = pixels[pix_x, pix_y][0]
            green = pixels[pix_x, pix_y][1]
            blue = pixels[pix_x, pix_y][2]
            ellipsebox = [(pix_x, pix_y), (pix_x + size, pix_y + size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(red, green, blue))
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        canvas.save(name + "_pointillism.png")
        self.ids.pic.source = name + "_pointillism.png"
    def sepia(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = int(pixels[x, y][0] * 0.393) + int(pixels[x, y][1] * 0.769) + int(pixels[x, y][2] * 0.189)
                green = int(pixels[x, y][0] * 0.349) + int(pixels[x, y][1] * 0.686) + int(pixels[x, y][2] * 0.168)
                blue = int(pixels[x, y][0] * 0.272) + int(pixels[x, y][1] * 0.534) + int(pixels[x, y][2] * 0.131)
                pixels[x, y] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_sepia.png")
        self.ids.pic.source = name + "_sepia.png"
    def pixelate(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for i in range(0, img.size[1] - 20, 20):
            for j in range(0, img.size[0] - 20, 20):
                red = pixels[j, i][0]
                green = pixels[j, i][1]
                blue = pixels[j, i][2]
                for k in range(i, i + 20):
                    for l in range(j, j + 20):
                        print(pixels[i, j])
                        pixels[k, l] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_pixelate.png")
        self.ids.pic.source = name + "_pixelate.png"





PhotoEditApp().run()