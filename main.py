from vision import Vision

#Instantiate vision object to look for objects with 8 vertices
vision = Vision(8)

while 1:
    print(vision.find())
