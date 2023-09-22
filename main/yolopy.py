from ultralytics import YOLO
import numpy as np

model = YOLO('/Users/nasir/Documents/3dprints/runs/segment/train6/weights/best.pt')

results = model('lpost1_convert.jpg')

print('number 1')
x, y = [], []

for r in results:
    data = np.array(r.masks.xy)
    coordinates_array = data[0]
    flat = [number for row in coordinates_array for number in row]
    pairs_list = [[flat[i], flat[i+1]] for i in range(0, len(flat), 2)]

    # Printing the list of pairs
    print(pairs_list)