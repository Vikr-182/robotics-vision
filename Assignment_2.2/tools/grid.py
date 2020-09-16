from utils import *
from constants import *
from imports import * 


def convertToString(num):
    a = str(num % 10)
    b = str(int(num / 10))
    c = str(int(num / 100))
    d = str(int(num / 1000))
    e = str(int(num / 10000))
    f = str(int(num / 100000))
    return f + e + d + c + b + a

def read_points():
    array = [[] for i in range(0,NUM_FILES)]
    for i in range(0,NUM_FILES):
       array[i] = readPointCloud(PATH_DATASET + "mydata/" + convertToString(i) + ".bin")
    return array

def read_poses():
    array = readData(PATH_DATASET + "dataset/01.txt")
    return array

if __name__ == "__main__":
    points = read_points()
    poses = read_poses()
    print(len(points))
    print(len(poses))
    actual_array = []
    for i in range(NUM_FILES):
        A = np.array(points[i])
        print(A.shape)
        B = np.array(
            [
            [poses[i][0],poses[i][1],poses[i][2],poses[i][3]],
            [poses[i][4],poses[i][5],poses[i][6],poses[i][7]],
            [poses[i][8],poses[i][9],poses[i][10],poses[i][11]]
            ]
            )
        #print(B.shape)
        #print("BAZINGA")
        C = np.dot(B,A.transpose()).transpose()
        #print(C.shape)
        #print(len(C))
        actual_array.append(C.tolist())
    print(len(actual_array))
    o3d.visualization.draw_geometries([np.array(actual_array)])

