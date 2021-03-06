import cv2
import numpy as np
from target import Target
import imutils

class Vision:
    def __init__(self, numCorners):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_EXPOSURE, -10) #Set exposure lower

        self.portraitModeSixInchAreaHexagonThing = 2800

        self.hsvValues = {
            "baseHue": 74,
            "hueRange": 10,
            "lowerSaturation": 200,
            "upperSaturation": 255,
            "lowerValue": 30,
            "upperValue": 200
        }

        self.numCorners = numCorners

        self.resX = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.resY = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    #Returns array of target objects, which contain points and area
    def find(self):
        #_, img = self.cap.read() #Get frame of video
        #ret, img = self.cap.read() #Get frame of video

        if(True):
                #print(self.cap.isOpened())
                if(not self.cap.isOpened()):
                        print("Opening cap")
                        self.cap.open(0)

        if (not self.cap.isOpened()):
                print("Not opened")
                quit()
        ret, img = self.cap.read()
        #print(img)

        img = cv2.rotate(img, cv2.ROTATE_180)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convert image to hsv for color detection

        #Lower and upper bounds of what is roughly green, will change later
        lower = np.array([self.hsvValues["baseHue"] - self.hsvValues["hueRange"], self.hsvValues["lowerSaturation"], self.hsvValues["lowerValue"]]) 
        upper = np.array([self.hsvValues["baseHue"] + self.hsvValues["hueRange"], self.hsvValues["upperSaturation"], self.hsvValues["upperValue"]]) 

        mask = cv2.inRange(hsv, lower, upper) #Color mask

        #Blur it to reduce noise, then expand it
        kernel = np.ones((1,1),np.uint8)
        #mask = cv2.erode(mask,kernel,iterations = 2)
        #mask = cv2.dilate(mask,kernel,iterations = 5)
        #mask = cv2.medianBlur(mask, 15) #Block size 15
        mask = cv2.GaussianBlur(mask, (15, 15), 0) #Block size 15

        #Get edges of image
        edges = cv2.Canny(img, 40, 100) #Lower bound 40, upper of 100

        otherEdges = cv2.Canny(img, 100, 200)

        otherEdges = cv2.bitwise_and(otherEdges, otherEdges, mask=mask)

        cv2.imshow("edges but good", otherEdges)
        filteredImg = cv2.bitwise_and(img, img, mask=mask)

        filteredImg = cv2.cvtColor(filteredImg, cv2.COLOR_BGR2GRAY)
        _, filteredImg = cv2.threshold(filteredImg, 20, 80, cv2.THRESH_BINARY)

        #Apply color mask to edges
        edges = cv2.bitwise_and(edges, edges, mask=mask)

        #Get contours of image
        cnts = cv2.findContours(filteredImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        cnts = imutils.grab_contours(cnts)

        #print(cnts)

        visionTargets = []
        areas = []

        for c in cnts:
            peri = cv2.arcLength(c, True) #Perimeter of contour
            area = cv2.contourArea(c) #Area of contour
            if area <= 10:
                break
            approx = cv2.approxPolyDP(c, 0.01 * peri, True) #Poly approximation of contour, epsilon of 1% perimeter
            #print(len(approx))
            if len(approx) == self.numCorners:
                #Append area and approx'ed points
                visionTargets.append(approx)
                areas.append(area)

        cv2.imshow("mask", mask)
        cv2.imshow("image", img)
        cv2.imshow("edges", edges)
        cv2.imshow("filtered", filteredImg)

        out = []
        for i in range(len(visionTargets)):
            out.append(Target(visionTargets[i], areas[i]))

        if cv2.waitKey(5) & 0xFF == 27:
            return out
        return out
        
