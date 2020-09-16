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
        B = poses[i].reshape(3,4)#np.array(
        C = np.dot(B,A.transpose()).transpose()
        print(C.shape)
        print("RARARAR")
        if i != 0:
            actual_array = np.concatenate((actual_array,C))
        else:
            actual_array = C
        

    print(len(actual_array))
    actual_array = np.array(actual_array)
    print(actual_array.shape)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(actual_array)
    o3d.visualization.draw_geometries([pcd])
