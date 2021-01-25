"""
This is the main file.  It calls the "findMatch" function from
Tyler.py.

Enter the path to an image, and it returns the best match.
"""

from Tyler import *



imageName = 'Supernova'

findMatch('testImages/QueryImg_'+imageName+'.jpg')



"""
Query Image File Names:
    Baby
    Dragon
    Test  # This should always fail to find a match
    Slug
    Bluelines
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
    Biden
    Fall
    Ghost
    AwesomeDay    
"""