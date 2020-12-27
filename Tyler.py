import numpy as np
import pickle
import cv2
import os
from matplotlib import pyplot as plt

from popsift import computeKp
from popsift import compare

"""self = str('QuerryImg_Baby.jpg')
userdes = computeKp(str('QuerryImg_Baby.jpg'))
f = open('monuments.pkl', 'rb')
tup = pickle.load(f)

maxp = -1
completed = 0
while (tup):
    print(tup[1])
    c = compare(userdes, tup[0], 0)

    if c > 0:
        if maxp < c:
            maxp = c
            self.qpath = tup[1]

    try:
        tup = pickle.load(f)
    except:
        if maxp != -1:
            print(self.qpath)
            ind = self.qpath.rfind("/")
            ind2 = -1
            for i in ['1', '2', '3', '4', '5']:
                ind2 = max(self.qpath.find(i), ind2)
            self.label_2.setText(
                "The image is of : " + self.qpath[ind + 1:ind2])
        else:
            self.label_2.setText("Sorry !No matches found")
        break"""

def annotate(self):
    #userdes = computeKp(str(self.file_name))
    userdes = computeKp(str(self))
    f = open('monuments.pkl', 'rb')
    tup = pickle.load(f)

    maxp = -1
    completed = 0
    while (tup):
        print(tup[1])
        c = compare(userdes, tup[0], 0)

        if c > 0:
            if maxp < c:
                maxp = c
                #self.qpath = tup[1]
                self = tup[1]

        try:
            tup = pickle.load(f)
        except:
            if maxp != -1:
                print(self.qpath)
                ind = self.qpath.rfind("/")
                ind2 = -1
                for i in ['1', '2', '3', '4', '5']:
                    ind2 = max(self.qpath.find(i), ind2)
                self.label_2.setText(
                    "The image is of : " + self.qpath[ind + 1:ind2])
            else:
                self.label_2.setText("Sorry !No matches found")
            break


annotate('QuerryImg_Baby.jpg')