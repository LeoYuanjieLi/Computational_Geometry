import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math

def preOrder(LTL, Points):
    angles = []
    for i in range(0, len(Points)):
        angle = getAngle(LTL, Points[i], rg.Point2d(-1, LTL.Y))
        angles.append(angle)

    return angles

def getAngle(srcPt, p1, p2):
    """Get Angle from 3 Points"""
    #   vector a (x, y) 
    va_x = p1.X - srcPt.X
    va_y = p1.Y - srcPt.Y
    
    #   vector b (x, y)
    vb_x = p2.X - srcPt.X
    vb_y = p2.Y - srcPt.Y
    
    #   production of 2 vectors
    productValue = (va_x * vb_x) + (va_y * vb_y)
    #    print("productValue", productValue)
    #   length va
    va_val = math.sqrt(va_x * va_x + va_y * va_y)
    #   length vb
    vb_val = math.sqrt(vb_x * vb_x + vb_y * vb_y)
    #   cos
    cosValue = productValue/(va_val * vb_val)
    if cosValue == 1:
        angle = 0
    elif cosValue == -1:
        angle = 180
    else:
        angle = math.acos(cosValue)*180/math.pi
    
    return angle

def sortPoints(Angles, Points):
    res = [x for _,x in sorted(zip(Angles,Points))]
    return res

def findExtreme(firstPt, secondPt, canPts):
    """first extrem point, second extrem point 
    and list of points as candidates, which are already sorted by angles"""
    # we need 2 stacks    
    stack_S = [firstPt, secondPt]

    stack_T = canPts


    while stack_T:

        currentSecondPt = stack_S[-1]
        currentFirstPt = stack_S[-2]
        nextPt = stack_T[-1]
        if isLeft(currentFirstPt, currentSecondPt, nextPt):
            stack_S.append(stack_T.pop())

        else:
            stack_S.pop()
    
    return stack_S



def isLeft(firstPt, secondPt, testPt):
    v1 = rg.Vector2d(firstPt.X - secondPt.X, firstPt.Y - secondPt.Y)
    v2 = rg.Vector2d(firstPt.X - testPt.X, firstPt.Y - testPt.Y)
    
    res = v1.X*v2.Y - v2.X*v1.Y

    return res > 0    




angles = preOrder(LTL, Points)
sortedPoints = sortPoints(angles, Points)

resultPoints = findExtreme(LTL, sortedPoints[-1], sortedPoints[:-1])
