import os

import cv2
import numpy as np

from function import *

path = 'E:\\Progress\\anicharts\\static\\images'
for file_name in os.listdir(path):
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    img = cv2.imread('E:\\Progress\\anicharts\\static\\images\\' + file_name)
    per_image_Bmean.append(np.mean(img[:, :, 0]))
    per_image_Gmean.append(np.mean(img[:, :, 1]))
    per_image_Rmean.append(np.mean(img[:, :, 2]))
    R = np.mean(per_image_Rmean)
    G = np.mean(per_image_Gmean)
    B = np.mean(per_image_Bmean)

    color_16 = ('{:02X}' * 3).format(round(R), round(G), round(B))
    name = dbf.find_one({'mid': int(file_name.split('.')[0])})['name']
    with open('E:\\Progress\\VideoHandle\\color.txt', 'a') as f:
        f.write(f"ani.colorPicker.setColor('{name}', '#{color_16}');\n")
