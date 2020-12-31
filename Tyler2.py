"""
This is the main file.  It calls the "findMatch" function from
Tyler.py.

Enter the path to an image, and it returns the best match.
"""

from Tyler import *



imageName = 'SB_Large'

findMatch('testImages/QueryImg_'+imageName+'.jpg')



"""
Query Image File Names:
    Baby
    Dragon
    Test  # This should always fail to find a match
    Slug  # This unfortunately returns the wrong rock (@ 70%, and >6)
    Bluelines  #This fails to find a match, but should not (@ 70%, and >6)
    Flower
    SB_Small
    SB_Large
    Abstract
    Bot1
    Bot2
    Cross
    Dots
    Flag
    Supernova
    Unicorn    
"""