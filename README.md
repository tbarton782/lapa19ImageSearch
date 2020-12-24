I cloned this from here (https://github.com/lapa19/Image-Search#image-search).  She has an almost identical project here (https://github.com/lapa19/Image-Annotation).  

What makes this code nifty is that it does exactly what we need... finds image matches in a database against a query image.  

I can't get the GUI to work, but after fixing some sloppy code, the writekp.py file works perfectly and creates a log/array/whatever, containing the keypoints of every image.  I think if we can strip out the GUI code, we could get it to work.  

---------------------


# Image-Search
This is an image search application developed with OpenCV's python interface. The user inputs an image of a monument and the applicaion searches for similar images and displays them. It uses SIFT algorithm for keypoint detection.Its GUI was designed with PyQt.

The popgui.py file contains the main code. The popsift.py contains code for using OpenCV's inbuilt SIFT algorithm. writekp.py contains code to store keypoints of each of the images in the database to a file.The instructions below assume that you have OpenCV installed.For OpenCV installation,visit http://goo.gl/OuJ1SW .To run the application, perform the following -

1.Make a folder monumentsdb which has images of monuments.Use name of the monument as name of the image.

2.Run writekp.py - python writekp.py .This detects keypoints of each of the images in monumentsdb and stores them to a file called monuments.pkl.It stores the name of the file and its corresponding keypoints.These keypoints are later read from the file during program execution.Instead of finding keypoints during each execution,we've stored them to a file to save execution time.

3.Run main code - python popgui.py. This will ask you to choose an image for search. Choose an image and it will display the result(s) after a few seconds.

4.This can be extended to other objects like images of books etc. as well. You can also make it a standalone executable with pyinstaller. Visit https://goo.gl/7b2hBA for more details.


