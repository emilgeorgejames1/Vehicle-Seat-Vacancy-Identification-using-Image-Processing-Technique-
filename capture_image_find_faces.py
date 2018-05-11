#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
# OpenCV program to detect face in real time
# import libraries of python OpenCV 
# where its functionality resides
import cv2 


# Load a cascade file for detecting faces
#xml file  used to find faces by frame
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
#xml file used to find eyes  by frame
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')


global_data = []


def capture_image_find_faces():
    #initialized camera port
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)
    if camera is None or not camera.isOpened():
        print('Warning: unable to open video source: ', camera_port)
    else:
        # loop runs if capturing has been initialized.
        while 1: 
         
            # reads frames from a camera
            ret, img = camera.read() 
         
            # convert to gray scale of each frames
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         
            # Detects faces of different sizes in the input image
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)
         
            for (x,y,w,h) in faces:
                # To draw a rectangle in a face 
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
         
                # Detects eyes of different sizes in the input image
                eyes = eye_cascade.detectMultiScale(roi_gray) 
         
                #To draw a rectangle in eyes
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
         
            # Display an image in a window
            cv2.imwrite("faces {0}.jpg".format(len(faces)),img)
     
            print "Found "+str(len(faces))+" face(s)"
            faces_found = str(len(faces))
            return faces_found
         
            # Wait for Esc key to stop
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
 
    # Close the window
    camera.release()
     
    # De-allocate any associated memory usage
    cv2.destroyAllWindows()  
 



