# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# Can modify this to work with webcam

import cv2
import numpy as np

def read_video(path_to_video):
    cap = cv2.VideoCapture(path_to_video)

    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
    ret = True     # cap.read() gives a boolean, ret val, and matrix of values

    for frame in range(0,frameCount-1):
        ret, buf[frame] = cap.read()

    return buf
