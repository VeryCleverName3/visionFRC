from vision import Vision
#from RioComms import RioComms

class VisionFRC():
    def __init__(self):
        self.TABLE_NAME = "angles"
        self.X_KEY_PREFIX = "xAngle"
        self.Y_KEY_PREFIX = "yAngle"
        self.SERVER_URL = "10.40.26.2"
        self.vision = Vision(8)
        self.targets = self.vision.find()
        #Constants for viewport's angle- needs to change still- in degrees
        self.VIEWPORT_ANGLE_X = 45
        self.VIEWPORT_ANGLE_Y = 30

    def readable(self):
        return self.vision.rawOut
    def runCommsCheck(self):
        self.send('test', 123)
        result = rioComms.receive(self.TABLE_NAME, 'test', 404)
        print("No Comms") if result == 404 else print ("Network Established")
        return (False if result == 404 else True)
        

    def send(self, key, value):
        rioComms.send(self.TABLE_NAME, key, value)

        #Instantiate vision object to look for objects with 8 vertices

        '''rioComms = RioComms(self.SERVER_URL)

        if (runCommsCheck()):

            while 1:
                self.targets = vision.find()

                send(self.X_KEY_PREFIX, 4026)
                
                if(len(targets) > 0):
                    value = self.targets[0].getAngleToCenterFromCamera(vision.resX, vision.resY, self.VIEWPORT_ANGLE_X, self.VIEWPORT_ANGLE_Y)
                    print(value[0])
                    send(self.X_KEY_PREFIX, value[0])
                    send(self.Y_KEY_PREFIX, value[1])
        '''
        while 1:
            self.targets = self.vision.find()