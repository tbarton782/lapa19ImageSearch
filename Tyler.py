"""
This module computes the keypoint descriptors of a query image, compares
them with the database (images.pkl), and returns the best match.

This module is called by "Tyler2.py".
"""

import pickle

from popsift import computeDesc
from popsift import compare


def findMatch(self):
    """Computes descriptors of query image > compares with database >
    returns best match """
    userdes = computeDesc(str(self))  # Finds descriptors of query image
    f = open('images.pkl', 'rb')
    tup = pickle.load(f)

    maxp = -1
    while (tup):
        print(tup[1])
        c = compare(userdes, tup[0], 0)  # Compares descriptors of query image with database

        if c > 0:
            if maxp < c:
                maxp = c
                self = tup[1]

        try:
            tup = pickle.load(f)
        except:
            if maxp != -1 and maxp >5:
                print()  # Blank line for readability
                print("and the winner is...", self)  # Prints the matching image
            else:
                print()  # Blank line for readability
                print("Sorry !No matches found")
            break
