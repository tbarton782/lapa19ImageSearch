"""
This module iterates through each image in the "imagesdb" directory,
extracts the keypoint descriptors, and saves them in a file (images.pkl)
for later use (to compare with the query image).
"""

import cv2
import pickle
import os

output = open('images.pkl', 'wb')

for f in os.listdir('imagesdb/'):
    print(f)
    img1 = cv2.imread(str(os.path.join('imagesdb/', f)), 0)
    h1, w1 = img1.shape[:2]
    img1 = cv2.resize(img1, (int(0.5 * w1), int(0.5 * h1)), interpolation=cv2.INTER_CUBIC)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    pickle.dump((des1, str(os.path.join('imagesdb/', f))), output, pickle.HIGHEST_PROTOCOL)

output.close()
