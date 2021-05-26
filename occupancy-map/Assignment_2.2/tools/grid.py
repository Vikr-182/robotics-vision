########################## LIBRARY IMPORTS ################################
from imports import * 
########################## CUSTOM IMPORTS #################################
from constants import *
from utils import *
from individual import createOccupancyGrid

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
        array[i] = readPointCloud(PATH_DATASET + "dataset/01/" + convertToString(i) + ".bin")[:,:3]
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

def createTotalOccupancyGrid(start_ind,size,points,poses):
    for ind in range(start_ind,start_ind + size):
        CM = np.array(CAMERA_TO_LIDAR)
        Y = points[ind][:, :3]
        Y = np.dot(CM[:, :3], Y.T).T
        vis = o3d.visualization.Visualizer()
        pcd = o3d.geometry.PointCloud()
        poses = readData(PATH_DATASET + "dataset/01.txt")
        poses =  poses[ind].reshape(3, 4)
        Y = np.dot(poses[:, :3], Y.T).T
        Y = Y + poses[:, 3]
        pcd.points = o3d.utility.Vector3dVector(Y)
        pcd = pcd.voxel_down_sample(voxel_size=3)
        Y = np.asarray(pcd.points)
        print(Y.shape)

        for point in Y:
            if inRange(int((point[0] + mini)) * STEP,XSIZ) and inRange(int((point[0] + mini) * STEP),XSIZ):
                matrix[int(point[0] + mini) * STEP, int(point[2] + mini) * STEP, :] += 1
    for i in range(int(1000/STEP)):
        for j in range(int(1000/STEP)):
            if np.sum(matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP, 0]) > THRESHOLD:
                matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP,:] = 200
            else :
                matrix[i*STEP: (i+1)*STEP, j*STEP:(j+1)*STEP,:] = 0

    cv2.imwrite(PNG_DESTINATION + convertToString(start_ind)  + "_SIZE" + str(size) +'.png', matrix)
    return matrix

def reduceMatrix(matrix):
    for i in range(XSIZ):
        for j in range(YSIZ):
            for k in range(ZSIZ):
                matrix[i][j][k] = math.floor(matrix[i][j][k]/THRESHOLD)
    return matrix

if __name__ == "__main__":
    points = read_points()                      # Gets a N x 3 array 
    poses = read_poses()                        # Gets all poses
    
    matrix = np.zeros(shape=(XSIZ,YSIZ,ZSIZ))
    save_poses = poses
    # FOR 5
    createTotalOccupancyGrid(0,5,points,save_poses)
    
    save_poses = poses
    # FOR 10
    createTotalOccupancyGrid(0,10,points,poses)

    save_poses = poses
    # FOR 15
    createTotalOccupancyGrid(0,15,points,poses)
