import rhinoscriptsyntax as rs
import random
import Rhino.Geometry as rg


def addNewPoints(Points, size):
    
    for i in range(0, size):
        pt = rg.Point2d(random.randrange(1,51), random.randrange(1,51))
        Points.append(pt)
    return Points


def getLTL(Points):
    LTL = Points[0]
    for i in range(1, len(Points)):
        if Points[i].Y < LTL.Y:
            LTL = Points[i]
        elif Points[i].Y == LTL.Y:
            if Points[i].X < LTL.X:
                LTL = Points[i]
    return LTL





newPoints = []
Points = addNewPoints(newPoints, 20)
LTL = getLTL(Points)
pts = []
for pt in Points:
    if pt.X == LTL.X and pt.Y == LTL.Y:
        continue
    else:
        pts.append(pt)





