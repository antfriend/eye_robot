import cv2
from video import create_capture
from common import clock, draw_str
import pygame,sys,os
from pygame.locals import *
import msvcrt
import sys

video_src = -1
cascade_fn = "haarcascade_frontalface_alty.xml"

window_x = 1600
window_y = 800
eyeball_size = 700
iris_size = 500
pupil_size = 300
sparkle_size = 70
  
def draw_eye(horizontal_pos):
  pygame.draw.circle(screen, (255,255,255), (horizontal_pos, window_y/2), eyeball_size, 0)
  pygame.draw.circle(screen, (0,255,0), (horizontal_pos, window_y/2), iris_size, 0)
  pygame.draw.circle(screen, (0,0,0), (horizontal_pos, window_y/2), pupil_size, 0)
  pygame.draw.circle(screen, (255,255,255), (window_x/3, window_y/3), sparkle_size, 0)

def eye_frame(horizontal_pos):
  black = (0,0,0)
  screen.fill(black) 
  draw_eye(horizontal_pos)
  pygame.display.flip()

def cam2eye_mapper(horizontal_pos):
  new_horizontal_pos = 0 - (horizontal_pos * 3)
  new_horizontal_pos = new_horizontal_pos + 1200
  return new_horizontal_pos

def close_eye():
  for i in range(100,0, -5):
    color = (i,i/2,i/3)
    screen.fill(color)
    pygame.time.delay(10)
    pygame.display.flip()
  color = (0,0,0)
  screen.fill(color)

def get_face_rectangle():
  ret, img = cam.read()
  # Do a little preprocessing:
  img_copy = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))
  gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  # Detect the faces, if any:
  return cascade.detectMultiScale(gray)
  
pygame.init()
window = pygame.display.set_mode((window_x, window_y)) 
pygame.display.set_caption('eyeball')
screen = pygame.display.get_surface()

cascade = cv2.CascadeClassifier(cascade_fn)
cam = create_capture(video_src)

left = 500
right = 1000
eye_is_open = False
while True:
  # Detect the faces, if any:
  rects = get_face_rectangle()
  
  if isinstance(rects, (list, tuple)) and not rects:
    if eye_is_open:
      eye_is_open = False
      close_eye()
      
  black = (0,0,0)
  screen.fill(black)

  for x, y, width, height in rects:
    eye_is_open = True
    draw_eye(cam2eye_mapper(x))
    #print "x=" + str(x) + " y=" + str(y) + " width=" + str(width) + " height=" + str(height)

  pygame.display.flip()
  
  
##  #go right
##  for num in range(left,right):
##    eye_frame(num)
##  #go left
##  for i in range(right,left, -1):
##    eye_frame(i)
  

sys.exit("get out of town")  


