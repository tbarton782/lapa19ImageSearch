"""
This code captures an image from the video stream from IPWebcam

https://www.studytonight.com/post/capture-videos-and-images-with-python-part2
"""

import cv2

videoCaptureObject = cv2.VideoCapture('http://192.168.86.52:8080/video')
result = True
while (result):
    ret, frame = videoCaptureObject.read()
    cv2.imwrite("../NewPicture.jpg", frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()



"""
This codes just shows the video stream

import cv2

videoCaptureObject = cv2.VideoCapture('http://192.168.86.52:8080/video')
while (True):
    ret, frame = videoCaptureObject.read()
    cv2.imshow('Capturing Video', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
"""