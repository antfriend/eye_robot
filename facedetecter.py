import cv2
from video import create_capture
from common import clock, draw_str
 
video_src = -1
cascade_fn = "haarcascade_frontalface_alty.xml"
#more: http://tutorial-haartraining.googlecode.com/svn/trunk/data/haarcascades/
#https://github.com/benosteen/FaceRecognition

# Create a new CascadeClassifier from given cascade file:
cascade = cv2.CascadeClassifier(cascade_fn)
cam = create_capture(video_src)

while True:
  ret, img = cam.read()
  # Do a little preprocessing:
  img_copy = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))
  gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  # Detect the faces, if any:
  rects = cascade.detectMultiScale(gray)
  # draw the rectangle:
  for x, y, width, height in rects:
    cv2.rectangle(img_copy, (x, y), (x+width, y+height), (255,0,0), 2)
    
    print "x=" + str(x) + " y=" + str(y) + " width=" + str(width) + " height=" + str(height)
    
  cv2.imshow('facedetect', img_copy)
  if cv2.waitKey(5) == 27:
    
    cam = ""
    cascade = ""
    cv2 = ""
    break
