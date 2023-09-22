#imports
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from PIL import Image
from sys import exit as finish
from orders import main as tsp
import matplotlib.style as mplstyle
from listsofstuff import thislist as variables
import numpy as np


#table and enviornment setup

global poly
files, prevx, prevy, prevz, poly = [], [], [], [], []
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
mplstyle.use('fast')

ax.set_xlim(0,957)

ax.set_ylim(0,720)

ax.set_zlim(0,5)

ax.set_xlabel('x')

ax.set_ylabel('y')

ax.set_zlabel('z')


#image inputs

while True:
    fileinput = input('Enter file name (write "Done" when finished!): ')
    if fileinput ==  'Done':
        if files == []:
            print('Input Error: You must enter at least one file!')
            finish()
        else:
            break
    else:
        try:
            fileinput = fileinput+'.jpg'
            im = Image.open(fileinput)
            files.append(fileinput)
        except:
            print('Invalid! Try again!')
            finish()

#image observatory
for images in files:
    X, Y, Z, limit = [], [], [], 240
    im = Image.open(images)
    pix, size = im.load(), im.size
    try:
        for x in range(size[0]):
            for y in range(size[1]):
                givenrgb = pix[x,y]
                if givenrgb[0]>limit and givenrgb[1]>limit and givenrgb[2]>limit:
                    X.append(x)
                    Y.append(y)
                    Z.append(files.index(images))
                    X, Y = tsp(X, Y)

                    vertices = [list(zip(X, Y, Z))]

                    poly.append(Poly3DCollection(vertices, alpha=0.8))

                    ax.add_collection3d(poly[-1])

                    thelist = [files.index(images)]*len(X)

                    if files.index(images) == 0:
                        prevx.append(X)
                        prevy.append(Y)
                        prevz.append(thelist)
                    else:
                        prevx.append(X)
                        prevy.append(Y)
                        prevz.append(thelist)
                        cross = [list(zip(prevx, prevy, prevz))]
                        global crosspoly
                        crosspoly = Poly3DCollection(cross, alpha=0.8)
                        ax.add_collection3d(crosspoly)
                        prevx, prevy, prevz = [], [], []
                        prevx.append(X)
                        prevy.append(Y)
                        prevz.append(thelist)

                    # ax.scatter(x, y, files.index(images))

    except TypeError:
        print('Sorry, this file is not compatible. Try to take a screenshot and try again.')



#ax.scatter(2,3,4) # plot the point (2,3,4) on the figure


plt.show()