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
        array[i] = readPointCloud(PATH_DATASET + "dataset/01/" + convertToString(i) + ".bin")
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

def inRange(val,maxVal):
    if val > 0 and val < maxVal:
        return 1
    return 0

def createOccupancyGrid(matrix,ind,points,poses):
    xstep=int(XSIZ/STEP)
    ystep=int(YSIZ/STEP)
    for point in points:
        if inRange(int((point[0] + mini)) * STEP,XSIZ) and inRange(int((point[0] + mini) * STEP),XSIZ):
            matrix[int(point[0] + mini) * STEP, int(point[2] + mini) * STEP, :] += 1
    for i in range(xstep):
        for j in range(ystep):
            if np.sum(matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP, 0]) > THRESHOLD:
                matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP,:] = 200
            else :
                matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP,:] = 0

    cv2.imwrite(PNG_DESTINATION + convertToString(ind) +'.png', matrix)
    return matrix

def reduceMatrix(matrix):
    for i in range(XSIZ):
        for j in range(YSIZ):
            for k in range(ZSIZ):
                matrix[i][j][k] = math.floor(matrix[i][j][k]/THRESHOLD)
    return matrix

def transform_matrix(ind,points,poses):
    CM = np.array(CAMERA_TO_LIDAR)
    Y = points[:, :3]
    Y = np.dot(CM[:, :3], Y.T).T
    vis = o3d.visualization.Visualizer()
    pcd = o3d.geometry.PointCloud()
    poses =  poses.reshape(3, 4)
    Y = np.dot(poses[:, :3], Y.T).T
    Y = Y + poses[:, 3]
    pcd.points = o3d.utility.Vector3dVector(Y)
    pcd = pcd.voxel_down_sample(voxel_size=3)
    Y = np.asarray(pcd.points)
    return Y

if __name__ == "__main__":
    points = read_points() # Gets a N x 3 array 
    poses = read_poses() # Gets all poses
    for ind in range(NUM_FILES):
        transformed = transform_matrix(ind,points[ind],poses[ind]);
        matrix = np.zeros(shape=(XSIZ, YSIZ, ZSIZ))
        matrix = createOccupancyGrid(matrix,ind,transformed,poses[ind])
