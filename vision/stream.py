from vision import Vision
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import time
import cv2


outputFrame = none
lock = threading.Lock()
app = Flask(__name__)
time.sleep(2.0)
vision = Vision(8)

@app.route("/")
def index():
    return render_template("index.html")




def start():
    while True:
		targets = vision.find()
