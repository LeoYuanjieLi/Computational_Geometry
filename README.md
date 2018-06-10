# Computational_Geography

This repo uses Python & C# Components to implement algorithms in computational geography

## 2 Line Intersect

 - Using `ToLeft` test to determine if 2 lines interesect in a plane(or space, same algorithm)

Grasshopper Python Implementation Sample:
![alt text](https://github.com/LeoYuanjieLi/Computational_Geography/blob/master/TwoLineIntersect/3d-case-1.JPG)
![alt text](https://github.com/LeoYuanjieLi/Computational_Geography/blob/master/TwoLineIntersect/3d-case-2.JPG)
![alt text](https://github.com/LeoYuanjieLi/Computational_Geography/blob/master/TwoLineIntersect/3d-case-3.JPG)


## Convex Hull

### Graham Scan Algorithm

- Basic idea (A brief illustration on GeeksforGeeks https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/): 

Let points[0..n-1] be the input array.

1) Find the bottom-most point by comparing y coordinate of all points. If there are two points with same y value, then the point with smaller x coordinate value is considered. Let the bottom-most point be P0. Put P0 at first position in output hull.

2) Consider the remaining n-1 points and sort them by polor angle in counterclockwise order around points[0]. If polor angle of two points is same, then put the nearest point first.

3 After sorting, check if two or more points have same angle. If two more points have same angle, then remove all same angle points except the point farthest from P0. Let the size of new array be m.

4) If m is less than 3, return (Convex Hull not possible)

5) Create an empty stack ‘S’ and push points[0], points[1] and points[2] to S.

6) Process remaining m-3 points one by one. Do following for every point ‘points[i]’
        4.1) Keep removing points from stack while orientation of following 3 points is not counterclockwise (or they don’t make a left turn).
            a) Point next to top in stack
            b) Point at the top of stack
            c) points[i]
         4.2) Push points[i] to S

5) Print contents of S

Grasshopper Python Implementation Sample:
![alt text](https://raw.githubusercontent.com/LeoYuanjieLi/Computational_Geography/master/Graham_Scan_Algorithm/Graham-Scan-Image.JPG)



## Water Runoff Similation

Recursively find the next point on the surface and then connect all points on a single stream.

- Sample in Grasshopper(Time Complexity: UpperBound O(n**2)):
![alt text](https://raw.githubusercontent.com/LeoYuanjieLi/Computational_Geography/master/WaterRunOff/img-1.JPG)
