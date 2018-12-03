class Line(object):
    def __init__(self, ptA, ptB, name):
        self.name = name
        self.upperPt = ptA if ptA[1] > ptB[1] else ptB
        self.lowerPt = ptA if ptA[1] < ptB[1] else ptB
        if ptA[1] == ptB[1]:
            if ptA[0] < ptB[0]:
                self.upperPt = ptA
                self.lowerPt = ptB
            else:
                self.upperPt = ptB
                self.lowerPt = ptA

    def __str__(self):
        return self.name


pointA = (-2, 2)
pointB = (1, 3)

testLine = Line(pointA, pointB, "s1")

print(testLine.upperPt)
print(testLine.lowerPt)
print(testLine)

