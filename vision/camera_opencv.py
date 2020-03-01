import os
import cv2
from base_camera import BaseCamera
from main import VisionFRC
vision = VisionFRC()


class Camera(BaseCamera):
    video_source = 0
    
    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        while True:
            # read current frame
            _, img = vision.readable()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
