import struct 
from Color import color

def char(c):# 1 bytes
    return struct.pack('=c',c.encode('ascii'))

def word(w):# 2 bytes
    return struct.pack('=h',w)

def dword(d):# 4 bytes
    return struct.pack('=l',d)

def write(self, filename, framebuffer):
        f = open(filename, 'bw')
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height*3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        for y in range(self.height):
            for x in range(self.width):
                #print(y, x)
                number = framebuffer[y][x]

                if number == 0:
                    f.write(color(0,0,0))

                if number == 1:
                    f.write(color(255,255,255))

                if number == 2:
                    f.write(color(255,0,0))

                if number == 3:
                    f.write(color(255,0,0))


        f.close()

def get_color_with_intensity(self, tx, ty, intensity):
        x = round(tx * self.width)
        y = round(ty * self.height)

        b = round(self.pixels[y][x][0] * intensity)
        g = round(self.pixels[y][x][1] * intensity)
        r = round(self.pixels[y][x][2] * intensity)

        return color(
            max(min(r, 255), 0),
            max(min(g, 255), 0),
            max(min(b, 255), 0))