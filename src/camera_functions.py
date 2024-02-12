import cv2
import imutils
import numpy as np
from imutils.video import VideoStream

def start_camera():
    return VideoStream(src=0).start()

def resize_frame(frame):
    return imutils.resize(frame, width=400)

def detect_faces(frame, net):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    return detections, (h, w)