from time import time
from PIL import Image
from convert import converttorgb as rgb

fileinput = input('enter file ')
start = time()
filename, saveas = fileinput+'.png', fileinput+'_convert.png'

im = Image.open(filename)
pix, size = im.load(), im.size

try:
    for x in range(size[0]):
        for y in range(size[1]):
           givenrgb = pix[x,y]
           wavelength = (100*(givenrgb[0]+givenrgb[1]+givenrgb[2]))+400
           color = rgb(wavelength)
           pix[x,y] = color
except TypeError:
    print('Sorry, this file is not compatible. Try to take a screenshot and try again.')
im.save(saveas)
end = time()
print(end-start)
