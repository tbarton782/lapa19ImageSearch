"""
This module contains the "compare" and "computeDesc" functions, called
by Tyler.py.
"""

import cv2


def compare(des1, des2, p):
    """Returns the number of matching descriptors"""
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)  # Tried Trees=1-500, did not change much
    search_params = dict(checks=50)  # Tried 1-1000, does not affect much

    # flann = cv2.FlannBasedMatcher(index_params, search_params)
    # matches = flann.knnMatch(des1, des2, k=2)
    bf = cv2.BFMatcher()  # Test of Brute-Force Matching
    matches = bf.knnMatch(des1, des2, k=2)  # Test Brute-Force Matching
    matchesMask = [[0, 0] for i in range(len(matches))]

    c = 0

    for i, (m, n) in enumerate(matches):
        if m.distance < 0.65 * n.distance:  # 65% seems to work best
            matchesMask[i] = [1, 0]
            c = c + 1

    # print("Number of matching descriptors =", c)
    # print()  # For readability

    print(c)  # The number of matching descriptors

    return c


def computeDesc(path):
    """Reads query image and returns the keypoint descriptors"""
    # Desriptors assign a numerical description to the area of the image the keypoint refers to
    img = cv2.imread(path)

    h1, w1 = img.shape[:2]
    img = cv2.resize(img, (int(0.50 * w1), int(0.50 * h1)),
                     interpolation=cv2.INTER_CUBIC)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img, None)
    return des1

# TODO: Tune FLANN according to https://www.docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html
# TODO: Try using Brute Force Matcher
