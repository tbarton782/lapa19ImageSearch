"""
This is the main file.  It calls the "findMatch" function from
Tyler.py.

Enter the path to an image, and it returns the best match.
"""

from Tyler import *



imageName = 'Baby'

findMatch('testImages/QueryImg_'+imageName+'.jpg')



"""
Query Image File Names:
    testImages/QueryImg_Baby.jpg
    testImages/QueryImg_Dragon.jpg
    testImages/QueryImg_Test.jpg  # This should fail to find a match
"""