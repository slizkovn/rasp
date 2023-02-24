#from __future__ import print_function
import numpy as np
import cv2
import glob
#from matplotlib import pyplot as plt
from common import *
import os

import sys


def splitfn(file_path):
    file_path_parts = file_path.split(sep=os.sep)
    _path = os.path.join(*file_path_parts[:-1])
    file_name = file_path_parts[-1]
    file_name_parts = file_name.split(sep='.')
    return _path, file_name_parts[0], file_name_parts[1]

img_names_undistort = [img for img in glob.glob(sys.argv[1])]
new_path = "/"

camera_matrix = np.array( [[2.21683667e+04, 0.00000000e+00, 1.20839386e+03],
 [0.00000000e+00, 1.90955028e+04, 6.41530623e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]);
dist_coefs = np.array([-1.05181947e+01, -4.46597883e+03, -2.48306773e-02, -1.96381917e-01, -2.28701265e+01]);

i = 0

#for img_found in img_names_undistort:
while i < len(img_names_undistort):
        img = cv2.imread(img_names_undistort[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        h,  w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

        dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

        # crop and save the image
        x, y, w, h = roi
        #dst = dst[y:y+h-50, x+70:x+w-20]

        name = img_names_undistort[i].split("/")
        print(name)
        #name = name[6].split(".")
        name = name[0]
        full_name = new_path + name + '.jpg'

        #outfile = img_names_undistort + '_undistorte.png'
        print('Undistorted image written to: %s' % full_name)
        cv2.imwrite(sys.argv[2], dst)
        i = i + 1