from vision import Vision

#Instantiate vision object to look for objects with 8 vertices
vision = Vision(8)

targets = vision.find()

while 1:
    targets = vision.find()
    # vision.find returns an array of vision target objects
    # targets[i].points are the vertices of the target
    # targets[i].area is the area of the target in pixels
def printTarget(target):
    print(target.points)
    
printTarget(targets[0])

    
