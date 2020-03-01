from vision import Vision
#from RioComms import RioComms
import remotecv


TABLE_NAME = "angles"
X_KEY_PREFIX = "xAngle"
Y_KEY_PREFIX = "yAngle"
SERVER_URL = "10.40.26.2"

#Constants for viewport's angle- needs to change still- in degrees
VIEWPORT_ANGLE_X = 45
VIEWPORT_ANGLE_Y = 30

def runCommsCheck():
    send('test', 123)
    result = rioComms.receive(TABLE_NAME, 'test', 404)
    print("No Comms") if result == 404 else print ("Network Established")
    return (False if result == 404 else True)
    

def send(key, value):
    rioComms.send(TABLE_NAME, key, value)

#Instantiate vision object to look for objects with 8 vertices
vision = Vision(8)

targets = vision.find()

'''rioComms = RioComms(SERVER_URL)

if (runCommsCheck()):

    while 1:
        targets = vision.find()

        send(X_KEY_PREFIX, 4026)
        
        if(len(targets) > 0):
            value = targets[0].getAngleToCenterFromCamera(vision.resX, vision.resY, VIEWPORT_ANGLE_X, VIEWPORT_ANGLE_Y)
            print(value[0])
            send(X_KEY_PREFIX, value[0])
            send(Y_KEY_PREFIX, value[1])
'''
while 1:
    targets = vision.find()