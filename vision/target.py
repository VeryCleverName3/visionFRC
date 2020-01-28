import math

class Target:
    def __init__(self, points, area):
        self.points = points
        self.area = area
        tempPoints = []

        for i in self.points:
            tempPoints.append(i[0])
        self.points = tempPoints
        self.STANDARD_WIDTH = 42 #Placeholder value
        self.PIXEL_TO_IN_CONV = 42 #Placeholder value
        self.RES_X = 1080 #Placeholder
        self.RES_Y = 720 #Placeholder
        self.FOV_X = 45 #Placeholder, degrees
        self.FOV_Y = 45 #Placeholder, degrees

    #Returns center point of vision target
    def getCenter(self):
        farPoints = self.getFurthestXPoints()
        avgX = farPoints[0][0] + farPoints[1][0]
        avgY = farPoints[0][1] + farPoints[1][1]

        return [avgX, avgY]

        return [avgX, avgY]

    #Returns normalized center point from [-1,1]. Takes resolution x and y as arguments
    def getNormalizedCenter(self, resX, resY):
        center = self.getCenter()

        avgX = center[0]
        avgY = center[1]

        avgX -= (resX / 2)
        avgX /= (resX / 2)

        avgY -= (resY / 2)
        avgY /= (resY / 2)

        return [avgX, avgY]

    #Returns angle to center of shape with theta=0 being straight ahead. resX and resY are resolution and viewAngle is the angle of the viewport in degrees 
    def getAngleToCenterFromCamera(self, resX, resY, viewAngleX, viewAngleY):
        return [(viewAngleX / 45) * math.atan(self.getNormalizedCenter(resX, resY)[0]) * 180 / math.pi, -(viewAngleY / 45) * math.atan(self.getNormalizedCenter(resX, resY)[1]) * 180 / math.pi]
    
    #TODO: This function- returns in something
    def getDistance():
        return (getYOffset()/math.tan((math.abs(getAngleToCenterFromCamera(self.RES_X, self.RES_Y, self.FOV_X, self.FOV_Y)[1]) * math.pi)/180)) / math.cos((math.abs(getAngleToCenterFromCamera(self.RES_X, self.RES_Y, self.FOV_X, self.FOV_Y)[0]) * math.pi)/180)
    
    #Returns the rotation of the vision target- counter clockwise is positive
    def getRotation():
        angle = math.acos(self.getCurrentPixelWidth() / self.getPixelNormalWidth())
        if self.getFurthestXPoints()[0][1] > self.getFurthestXPoints()[1][1]:
            angle *= -1
        return angle

    #Returns farthest x and y points
    def getFurthestXPoints():
        leftPoint = self.getCenter()[0]
        rightPoint = leftPoint
        for i in self.points:
            if i[0] < leftPoint:
                leftPoint = i
            if i[0] > rightPoint:
                rightPoint
        return [leftPoint, rightPoint]
    
    #Returns max width of target based on distance
    def getNormalWidth():
        return self.STANDARD_WIDTH / self.getDistance()

    def getPixelNormalWidth():
        return self.getNormalWidth() * self.PIXEL_TO_IN_CONV

    def getCurrentPixelWidth():
        points = self.getFurthestXPoints()
        return math.sqrt(((points[0][0] - points[1][0]) * (points[0][0] - points[1][0])) + ((points[0][1] - points[0][1]) * (points[0][1] - points[0][1])))
