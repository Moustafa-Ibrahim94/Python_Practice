Python Exercise Requirements:

Given a 2D room and a set of line segments each described by two 2D points:

1. Write a function which returns the line segment closest to a given point (origin) in a given direction (angle in degrees).
2. Identify all relevant test cases and write unit tests for them.
3. Add type hints to all your functions and variables


My Approach:
    
1. build a line with the knowledge of point and angle (Origin line)
2. find the intersection point between two lines (Origin line - line segment).
3. then, find the distance between the intersecting point and origin point to use in finding the closest line segment.
4. finally, get the min distance and give me the line segment.


you will see three files:
1. Intersect_Function.py
2. main.py
3. test_app.py

lets go in every file and we will start with the the function file
1. Intersect_Function.py 
        - we are having here the origin point which is (0,0) and i called point0.
        - and 1ine which consist of two points, line1 = {point1,point2}.
        - then the x and y for each point.
        - angle in degrees
    these things are give, from it we can get the intersect between origin line and line segment 
    then calculate the distance between intersect point and origin point to find later the min distance
    this function should take angle in degrees as int, ex: 45 and line as set, ex: {(1,-1),(1,1)} and
    return a tuple consist of two points and the distance between origin point and line segment  like ({(1, 1), (1, -1)}, 1.41)
    that output means the distance between line1 and origin point will equal to 1.41 when the angle = 45
    then we will go to  main.py
2. main.py
        - in the main file we will define many line segments, for example: line_1 = {(1, -1), (1, 1)}, line_2 = {(2, -1), (2, 1)}
        - then we will puts these lines inside a list, for example: lines = [line_1, line_2, line_3]
        - then we will iterate through the lines and pass each line to the intersec_distance function
        - and that should return the line and the distance between origin point and that line
        - we will put the out put in a list called dist_list then print the closest line segment 
          using this line of code: print(min(dist_list, key=lambda t: t[1]))
        - now we got our closest line to the point of origin when the angle equal 45
        
 


