# Given an array of points on the X-Y plane points where points[i] = [xi, yi], 
# return the area of the largest triangle that can be formed by any three different points. 
# Answers within 10-5 of the actual answer will be accepted.

##### Example 1 #####
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest

##### Example 2 #####
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000

#####################

def largestTriangleArea(points) -> float:
        
    def schoelaceFormula(p1, p2, p3):
        return 0.5 * abs(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]) )
    max_area = 0

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                p1, p2, p3 = points[i], points[j], points[k]
                # Tuples
                area = schoelaceFormula(p1, p2, p3)
                if area > max_area:
                        max_area = area

    return max_area

points1 = [[0,0],[0,1],[1,0],[0,2],[2,0]]
points2 = [[1,0],[0,0],[0,1]]

print(f"The area of the largest triangle possible with these points({points1} is: {largestTriangleArea(points1)})")
print(f"The area of the largest triangle possible with these points({points2} is: {largestTriangleArea(points2)})")

