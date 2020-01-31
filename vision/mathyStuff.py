import math

def getMotorVelocity(targetHeight, displacementFromTarget, robotVelocity):
    g = 9.806
    y0 = -targetHeight
    d = displacementFromTarget
    vr = robotVelocity
    o = math.pi / 4
    h = math.pi * 3 / 4

    v0 = (1/math.cos(o))*math.sqrt((g*(d*d))/(2*((d*math.tan(o)) + y0)))
    vm = math.sqrt((vr * vr)+((v0-(math.cos(h) * vr))) * (v0-(math.cos(h) * vr)))
    a = math.asin(vr / v0)

    print("v0, " + str(v0))
    print("vm, " + str(vm))
    print("a, " + str(a))


getMotorVelocity(2.49, 7, 2)
