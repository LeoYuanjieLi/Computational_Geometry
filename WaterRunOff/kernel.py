import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import math

#global variables

inputPtsData = gh.DivideSurface(Surface, Density, Density)
inputPts = inputPtsData[0]
inputNorms = inputPtsData[1]
inputUV = inputPtsData[2]





def runoffPts(inputPts, Surface, DistanceFactor=1.0, threshold=50):
    outputCrvs = []
    pts = inputPts
    norms = inputNorms
    #loop through all points in the input list    
    for pt in pts:
        curve = generatePts(pt, Surface, DistanceFactor, threshold)
        outputCrvs.append(curve)

    return outputCrvs 


def generatePts(orgPt, Surface, DistanceFactor, threshold):
    count = 0
    movedPtList = []
    inputPt = orgPt
    
    while count < threshold:
        data = nextPt(inputPt, Surface, DistanceFactor)
        if not data:
            curve = rg.PolylineCurve(movedPtList)
            return curve 

        elif isinstance(data, rg.Point3d):
            newPt = data
        elif isinstance(data, list):
            newPt = data[1]

        
        if newPt.Z >= inputPt.Z:
            break
        
        if newPt.X == inputPt.X and newPt.Y == inputPt.Y:
            curve = rg.PolylineCurve(movedPtList)
            return curve
        
        movedPtList.append(newPt)
        inputPt = newPt
        count += 1
     
    curve = rg.PolylineCurve(movedPtList)
    return curve

def nextPt(pt, surface, DistanceFactor):
    boolean,u,v = Surface.ClosestPoint(pt)
    norm = Surface.NormalAt(u,v)
    unitNormLine = gh.LineSDL(pt, norm, DistanceFactor)
    ptToProject = gh.EndPoints(unitNormLine)
    ProjectedPt = gh.ProjectPoint(ptToProject, -gh.UnitZ(), Surface)[0]
    
    return ProjectedPt



#tests:

#test 1 print inputPts element


#test 2 testing nextPt method

#b = (nextPt(inputPts[33], Surface, 1.0))

#test 3 testing generatePts method

# a = generatePts(inputPts[222], Surface, 1.0, 300)

runoff = []
for pt in inputPts:
    runoff.append(generatePts(pt, Surface, DistanceFactor, threshold))

    


#c = runoffPts(inputPts, Surface, 1.0, 50)