import numpy as np
from scipy.spatial import Delaunay
from stl import mesh
from sys import exit as finish
from PIL import Image
from ultralytics import YOLO
from tqdm import tqdm

# points
num_points = 100
files, X, Y, Z = [], [], [], []

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

for images in tqdm(files, desc='YOLO Inference: '):
    model = YOLO('/Users/nasir/Documents/3dprints/runs/segment/train6/weights/best.pt')

    results = model(images, verbose=False)

    for r in results:
        data = np.array(r.masks.xy)
        coordinates_array = data[0]
        flat = [number for row in coordinates_array for number in row]
        noz = 0
        for val in flat:
            if flat.index(val) % 2 == 0:
                X.append(val)
                noz += 1
            else:
                Y.append(val)
                noz += 1

        for x in range(int(noz/2)):
            Z.append(files.index(images)*100)
        



    # limit = 230
    # im = Image.open(images)
    # pix, size = im.load(), im.size
    # try:
    #     for x in range(size[0]):
    #         for y in range(size[1]):
    #             givenrgb = pix[x,y]
    #             if givenrgb[0]>limit and givenrgb[1]>limit and givenrgb[2]>limit:
    #                 X.append(x)
    #                 Y.append(y)
    #                 Z.append(files.index(images)*100)

    # except TypeError:
    #     print('Sorry, this file is not compatible. Try to take a screenshot and try again.')

pts = np.array([X, Y, Z]).T 

# perform delaunay triangulation
triangulation = Delaunay(pts)

# vertices and faces from the delaunay alg
vertices = pts
faces = triangulation.simplices

# mesh
random_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
for i, f in tqdm(enumerate(faces), desc='Final Processing: '):
    for j in range(3):
        random_mesh.vectors[i][j] = vertices[f[j], :]

# save
random_mesh.save('result.stl')

print('Zain, the program was a success!')