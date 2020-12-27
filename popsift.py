import numpy as np
import cv2, os
from matplotlib import pyplot as plt


def compare(des1, des2, p):
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    matchesMask = [[0, 0] for i in xrange(len(matches))]

    c = 0

    for i, (m, n) in enumerate(matches):
        if m.distance < 0.59 * n.distance:
            matchesMask[i] = [1, 0]
            c = c + 1

    print "In sift :Matches :", c

    return c


def computeKp(path):
    img = cv2.imread(path)

    h1, w1 = img.shape[:2]
    img = cv2.resize(img, (int(0.8 * w1), int(0.8 * h1)), interpolation=cv2.INTER_CUBIC)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img, None)
    return des1
