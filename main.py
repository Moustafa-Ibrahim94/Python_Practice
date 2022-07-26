import Intersect_Function

line_1 = {(1, -1), (1, 1)}
line_2 = {(2, -1), (2, 1)}

lines = [line_1, line_2]
angle = 0
dist_list = []
# iterate through every line
for line in lines:
    # get the distance and save it in dist_list as (line1,distance)
    dist_list.append(Intersect_Function.intersect_distance(angle, line))

# filter None values from my dist_list --> None values represent no intersect
print(dist_list)
dist_list = list(filter(None, dist_list))

# then print the closest line segment
if len(dist_list) == 0:
    print("No Intersections")
else:
    print(min(dist_list, key=lambda t: t[1])[0])
    # Output = {(1, 1), (1, -1)}
