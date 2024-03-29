"""
-------------------- DESCRIPTION ------------------
This is a
------------------ DATE & AUTHOR ------------------
12/22/2020, Tyler

------------------- HELPFUL LINKS -----------------

---------------------------------------------------
"""

import cv2 as cv
import matplotlib.pyplot as plt


def compare_images(image1, image2):
    img1 = cv.imread(image1, cv.IMREAD_GRAYSCALE)  # queryImage
    img2 = cv.imread(image2, cv.IMREAD_GRAYSCALE)  # trainImage

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # Find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.65 * n.distance:  # Filters out weak (large distance) matches
            good.append([m])
            print(m.distance)  # for testing only

    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None,
                             flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.imshow(img3), plt.show()

    # Calculate the number of matching good features, tb
    print(len(good))
    print(good)  # for testing only
