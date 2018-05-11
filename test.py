#!/usr/bin/python
# -*- coding: utf-8 -*-

def capture_image_find_faces():
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)
    if camera is None or not camera.isOpened():
        # print('Warning: unable to open video source: ', camera_port)
        frame = cv2.imread("data/face.jpg", 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        print "Found "+str(len(faces))+" face(s)"
        faces_found = str(len(faces))
        return faces_found
    		


