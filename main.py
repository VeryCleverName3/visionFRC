import cv2
import numpy as np
import keyboard
import imutils

cap = cv2.VideoCapture(0)

value = 70

portraitModeSixInchAreaHexagonThing = 2800

hsvValues = {
    "baseHue": 70,
    "hueRange": 20,
    "lowerSaturation": 10,
    "upperSaturation": 250,
    "lowerValue": 10,
    "upperValue": 250
}

while 1:
    _, img = cap.read()

    if keyboard.is_pressed("q"):
        value += 1
        print(value)

    cap.set(cv2.CAP_PROP_EXPOSURE, -10)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([hsvValues["baseHue"] - hsvValues["hueRange"], hsvValues["lowerSaturation"], hsvValues["lowerValue"]]) 
    upper = np.array([hsvValues["baseHue"] + hsvValues["hueRange"], hsvValues["upperSaturation"], hsvValues["upperValue"]]) 

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.medianBlur(mask, 15)

    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    edges = cv2.Canny(img, 40, 100)

    edges = cv2.bitwise_and(edges, edges, mask=mask)

    cnts = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)

    foundRectangle = False

    visionTargets = []
    areas = []

    for c in cnts:
        M = cv2.moments(c)
        if(M["m00"] != 0):
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True)
            #print(len(approx))
            #print(approx)
            if len(approx) == 8:
                foundRectangle = True
                visionTargets.append(approx)
                areas.append(cv2.contourArea(c))

    if foundRectangle:
        print(areas)
    else:
        print("No Vision. :(")

    cv2.imshow("mask", mask)
    cv2.imshow("image", img)
    cv2.imshow("edges", edges)

    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()
