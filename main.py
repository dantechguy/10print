from random import randint as rnd
from PIL import Image


# 2736, 1824
# init vars
hor_res = 512
ver_res = 512
chr_wid = 16

hor_chr = hor_res // chr_wid
ver_chr = ver_res // chr_wid

# start
width = hor_chr * chr_wid
height = ver_chr * chr_wid


image = Image.new('1', (width, height))
pixels = image.load()

def create_backslash(x, y, pixels, size):
    for pixel in range(size):
        slash_x = x + pixel
        slash_y = y + pixel
        pixels[slash_x, slash_y] = 1

def create_forwardsslash(x, y, pixels, size):
    temp_x = x + size - 1
    for pixel in range(size):
        slash_x = temp_x - pixel
        slash_y = y + pixel
        pixels[slash_x, slash_y] = 1

for y in range(ver_chr):
    for x in range(hor_chr):
        slash_type = rnd(0, 1)
        chr_x = x * chr_wid
        chr_y = y * chr_wid
        if slash_type == 1:
            create_backslash(chr_x, chr_y, pixels, chr_wid)
        else:
            create_forwardsslash(chr_x, chr_y, pixels, chr_wid)

image.save('10print.png')