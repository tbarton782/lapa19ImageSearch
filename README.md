I cloned this from here (https://github.com/lapa19/Image-Search#image-search).  She has an almost identical project here (https://github.com/lapa19/Image-Annotation).  

I basically peeled off all of the GUI code because I could not get it to work, fixed a bunch of sloppy code, and customized it for our use case.  

How it works:

1.  Images are stored in "imagesdb"
2.  writekp.py extracts the keypoint descriptors, and saves them in a file (images.pkl) for later use
3.  Tyler2.py takes a query image as input, and returns the best match