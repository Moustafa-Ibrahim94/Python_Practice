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
