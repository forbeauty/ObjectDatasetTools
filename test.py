import cv2
import numpy as np
import skimage
depth_filename="LINEMOD/duck/depth/400.png"
imgOri = cv2.imread(depth_filename, -1)
depth=cv2.split(imgOri)[0]
depth[depth>2000]=0
depth=depth/2000.0000
cv2.imshow('imgOri',depth)
cv2.waitKey(0)