def main(X, Y):
    import numpy as np
    import matplotlib.pyplot as plt
    coo = liststocoords(X, Y)
    tours = nearest_neighbor_tsp(coo)
    pathcoords = []
    for x in tours:
        locat = coo[x]
        pathcoords.append(locat)
    finalx, finaly = coordstolists(pathcoords)
    return finalx, finaly

def euclidean_distance(p1, p2):
    import numpy as np
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tsp(points, start_idx=0):
    n = len(points)
    remaining_points = list(range(n))
    tour = [start_idx]
    remaining_points.remove(start_idx)

    while remaining_points:
        nearest_idx = min(remaining_points, key=lambda idx: euclidean_distance(points[tour[-1]], points[idx]))
        tour.append(nearest_idx)
        remaining_points.remove(nearest_idx)

    tour.append(start_idx)  # Return to the starting point to complete the loop
    return tour

def liststocoords(X, Y):
    coordinates = list(zip(X, Y))
    return coordinates

def coordstolists(coords):
    x_values, y_values = zip(*coords)
    x_values_list = list(x_values)
    y_values_list = list(y_values)
    return x_values_list, y_values_list
