using Rhino;
using Rhino.Geometry;
using Rhino.DocObjects;
using Rhino.Collections;

using GH_IO;
using GH_IO.Serialization;
using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper.Kernel.Types;

using System;
using System.IO;
using System.Xml;
using System.Xml.Linq;
using System.Linq;
using System.Data;
using System.Drawing;
using System.Reflection;
using System.Collections;
using System.Windows.Forms;
using System.Collections.Generic;
using System.Runtime.InteropServices;



/// <summary>
/// This class will be instantiated on demand by the Script component.
/// </summary>
public class Script_Instance : GH_ScriptInstance
{
#region Utility functions
  /// <summary>Print a String to the [Out] Parameter of the Script component.</summary>
  /// <param name="text">String to print.</param>
  private void Print(string text) { /* Implementation hidden. */ }
  /// <summary>Print a formatted String to the [Out] Parameter of the Script component.</summary>
  /// <param name="format">String format.</param>
  /// <param name="args">Formatting parameters.</param>
  private void Print(string format, params object[] args) { /* Implementation hidden. */ }
  /// <summary>Print useful information about an object instance to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj) { /* Implementation hidden. */ }
  /// <summary>Print the signatures of all the overloads of a specific method to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj, string method_name) { /* Implementation hidden. */ }
#endregion

#region Members
  /// <summary>Gets the current Rhino document.</summary>
  private readonly RhinoDoc RhinoDocument;
  /// <summary>Gets the Grasshopper document that owns this script.</summary>
  private readonly GH_Document GrasshopperDocument;
  /// <summary>Gets the Grasshopper script component that owns this script.</summary>
  private readonly IGH_Component Component;
  /// <summary>
  /// Gets the current iteration count. The first call to RunScript() is associated with Iteration==0.
  /// Any subsequent call within the same solution will increment the Iteration count.
  /// </summary>
  private readonly int Iteration;
#endregion

  /// <summary>
  /// This procedure contains the user code. Input parameters are provided as regular arguments,
  /// Output parameters as ref arguments. You don't have to assign output parameters,
  /// they will have a default value.
  /// </summary>
  private void RunScript(Curve x, Curve y, ref object Intersect, ref object A, ref object B)
  {
    Point3d pt1 = new Point3d(x.PointAtStart.X, x.PointAtStart.Y, x.PointAtStart.Z);
    Point3d pt2 = new Point3d(x.PointAtEnd.X, x.PointAtEnd.Y, x.PointAtEnd.Z);
    Point3d pt3 = new Point3d(y.PointAtStart.X, y.PointAtStart.Y, y.PointAtStart.Z);
    Point3d pt4 = new Point3d(y.PointAtEnd.X, y.PointAtEnd.Y, y.PointAtEnd.Z);

    Intersect = isIntersect(pt1, pt2, pt3, pt4);

  }

  // <Custom additional code> 
  bool isLeft(Point2d Pt_A, Point2d Pt_B, Point2d Pt_C){

    Vector2d v1 = new Vector2d(Pt_A.X - Pt_B.X, Pt_A.Y - Pt_B.Y);
    Vector2d v2 = new Vector2d(Pt_A.X - Pt_C.X, Pt_A.Y - Pt_C.Y);

    double result = v1.X * v2.Y - v2.X * v1.Y;

    return result > 0;

  }


  bool isIntersect(Point3d pt1, Point3d pt2, Point3d pt3, Point3d pt4) {
    //if two line segment intersect, they have to be on the same plane.
    Plane plane123 = new Plane(pt1, pt2, pt3);
    double val = plane123.DistanceTo(pt4);

    bool isOnPlane = (val - 0 < 0.0001);
    bool testA;
    bool testB;
    Point2d pj1 = new Point2d(0, 0);
    Point2d pj2 = new Point2d(0, 0);
    Point2d pj3 = new Point2d(0, 0);
    Point2d pj4 = new Point2d(0, 0);
    if(!isOnPlane){

      bool res = false;
      return res;
    }
    else {
      //project 2 line segment onto XY Plane, if the projected line segment intersects, the origin
      //line segment intersect as well

      pj1.X = pt1.X;
      pj1.Y = pt1.Y;
      pj2.X = pt2.X;
      pj2.Y = pt2.Y;
      pj3.X = pt3.X;
      pj3.Y = pt3.Y;
      pj4.X = pt4.X;
      pj4.Y = pt4.Y;

      if((pj1.X == pj3.X && pj1.Y == pj3.Y) || (pj1.X == pj4.X && pj1.Y == pj4.Y) ||
      (pj2.X == pj3.X && pj2.Y == pj3.Y) || (pj2.X == pj4.X && pj2.Y == pj4.Y)) {

        return true;
      }



      testA = isLeft(pj1, pj2, pj3) != isLeft(pj1, pj2, pj4);

      testB = (isLeft(pj3, pj4, pj1) != isLeft(pj3, pj4, pj2));

      bool res = testB;
      return res;
    }
  }
  // </Custom additional code> 
}