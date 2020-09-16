########################## LIBRARY IMPORTS ################################
from imports import * 
########################## CUSTOM IMPORTS #################################
from constants import *
from utils import *

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


def save_png(matrix,ind):
    cv2.imwrite(PNG_DESTINATION + convertToString(ind) + ".png",matrix)
    return True

def get_val(val):
    VAL = math.floor(abs(val))
    return VAL

def createOccupancyGrid(matrix,ind,points,poses):
    Y = np.array(points)
    CL = np.array(CAMERA_TO_LIDAR)
    Y = np.dot(CL,Y.T).T
    print(Y.shape)
    Y = np.dot(poses.reshape(3,4),Y.T).T
    for i in range(len(points)):
        Y = points[i]
        if get_val(Y[0] + MAX[0]) < MAX[0] and get_val(Y[0] + MAX[0]) > MIN[0]:
            if get_val(Y[1] + MAX[1]) < MAX[1] and get_val(Y[1] + MAX[1]) > MIN[1]:
                if get_val(Y[2] + MAX[2]) < MAX[2] and get_val(Y[2] + MAX[2]) > MIN[0]:
                    matrix[get_val(Y[0] + MAX[0])][get_val(Y[1] + MAX[1])][get_val(Y[2] + MAX[2])] = matrix[get_val(Y[0] + MAX[0])][get_val(Y[1] + MAX[1])][get_val(Y[2] + MAX[2])] + 1
    return matrix
        #print(Y[i].shape)

def reduceMatrix(matrix):
    for i in range(XSIZ):
        for j in range(YSIZ):
            for k in range(ZSIZ):
                matrix[i][j][k] = math.floor(matrix[i][j][k]/THRESHOLD)
    return matrix

if __name__ == "__main__":
    matrix = np.zeros(shape=(XSIZ,YSIZ,ZSIZ));
    points = read_points()
    poses = read_poses()
    for ind in range(1):
        matrix = createOccupancyGrid(matrix,ind,points[ind],poses[ind])
        matrix = reduceMatrix(matrix);
        save_png(matrix,ind)
