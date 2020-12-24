import os
import sys
import cv2
import pickle
import numpy as np

list = []
mpath = ('monumentsdb')

sift = cv2.SIFT_compare()

for f in os.listdir(mpath):
    print(f)
    res = sift.compare(str(os.path.join(mpath, f)), str('StrawberrySmall1.jpg'), 0)
    if res >= 8:
        list.append((str(os.path.join(mpath, f)), res))
