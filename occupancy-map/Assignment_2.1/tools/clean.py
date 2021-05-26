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

def check(key,val,MIN_VAL,MAX_VAL):
    if val < MIN_VAL or val > MAX_VAL:
        return 1
    return key

def filter(array):
    barray = []
    for i in range(len(array)):
        print("i=")
        print(i)
        carray = []
        print("BEFORE")
        print(len(array[i]))
        for j in range(len(array[i])):
            key = 0
            for k in range(len(array[i][j])):
                key = check(key,array[i][j][k],MIN[k],MAX[k])
            if key == 0:
                carray.append(array[i][j])
        barray.append(carray)
        fil = open(PATH_MY_DATASET + "mydata/" + convertToString(i) + ".bin","wb")
        carray = np.array(carray)
        np.save(fil,carray)
        fil.close()
    return barray

def read_points():
    array = [[] for i in range(0,NUM_FILES)]
    for i in range(0,NUM_FILES):
       array[i] = readPointCloud(PATH_DATASET + "dataset/01/" + convertToString(i) + ".bin")
    return array

def read_poses():
    array = readData(PATH_DATASET + "dataset/01.txt")
    return array

def transform_matrix(points,poses):
    CL = np.array(CAMERA_TO_LIDAR)
    poses = np.array([
                [poses[0],poses[1],poses[2],poses[3]],
                [poses[4],poses[4],poses[6],poses[7]],
                [poses[8],poses[9],poses[10],poses[11]],
                [0,0,0,1]
            ])
    Y = np.array(points)
    Y = np.dot(CL,Y.T).T
    Y = np.dot(poses,Y.T).T
    return Y


if __name__ == "__main__":
    print("LOLA")
    points = read_points()
    poses = read_poses()
    for i in range(NUM_FILES):
        points[i] = transform_matrix(points[i],poses[i])
    print(len(poses))
    print(filter(points))