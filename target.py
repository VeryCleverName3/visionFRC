import math

class Target:
    def __init__(self, points, area):
        self.points = points
        self.area = area
        tempPoints = []

        for i in self.points:
            tempPoints.append(i[0])
        self.points = tempPoints

    #Returns center point of vision target
    def getCenter(self):
        avgX = 0
        avgY = 0
        for i in self.points:
            avgX += i[0]
            avgY += i[1]
        avgX /= len(self.points)
        avgY /= len(self.points)

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
    
    #TODO: This function- returns in inches
    def getDistance():
        return 12
    
    #Returns 
    def getRotation():
        return "hi"