import Rhino.Geometry as rg

lines = []

for i in range(0, len(Pts)-1):
    line = rg.Line(Pts[i], Pts[i+1])
    lines.append(line)
lastLine = rg.Line(Pts[-1], Pts[0])
lines.append(lastLine)