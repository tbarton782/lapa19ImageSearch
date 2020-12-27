import numpy as np
import cv2, os
from matplotlib import pyplot as plt

from popsift import compare
from popsift import computeKp

userdes = popsift.computeKp(str(QuerryImg_Baby))
f = open('monuments.pkl', 'rb')
tup = pickle.load(f)

maxp = -1
completed = 0
prev = time.time()
while (tup):
    self.val = self.val + float(100) / 29
    self.progressBar.setProperty("value", self.val)
    print(tup[1])
    c = popsift.compare(userdes, tup[0], 0)
    print(time.ctime())

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
        break
now = time.time()
print("Total time elapsed :", now - prev)
