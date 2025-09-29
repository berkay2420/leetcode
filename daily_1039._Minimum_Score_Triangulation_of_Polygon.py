# You have a convex n-sided polygon where each vertex has an integer value. 
# You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

# Polygon triangulation is a process where you divide a polygon into a set of triangles 
# and the vertices of each triangle must also be vertices of the original polygon.
# Note that no other shapes other than triangles are allowed in the division. 
# This process will result in n - 2 triangles.

# You will triangulate the polygon. 
# For each triangle, the weight of that triangle is the product of the values at its vertices. 
# The total score of the triangulation is the sum of these weights over all n - 2 triangles.

# Return the minimum possible score that you can achieve with some triangulation of the polygon.


# Example 1:
# Input: values = [1,2,3]
# Output: 6
# Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

# Example 2:
# Input: values = [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
# The minimum score is 144.

# Example 3:
# Input: values = [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13

#############################################


from functools import cache


def minScoreTriangulation(values):

    #Triangulation is drawing lines between corners to create triangles inside shape
    #But lines cannot intersect
    #Score (weight) edge1 * edge2 * edge3

    # Solution is breaking the problem into smaller problems using dynamic programming
    # dp(i,j) --> min score to triangulate the sub-polygon from vertex i to vertex j
    # store (memorize) the results to avoid re-calculating

    # Pick a middle vertex "k"  where i<k<j. This way we have 2 sub-polygon / 2 smaller problems
    # (i,,,,k) and (k,,,,j) 

    # Minimum score is min(score(i,j,k) + dp(i,k) + dp(k,j))

    @cache #Storing the results
    def minTriangulationScore(i,j):

        if j < i + 2:
            return 0
            #J is in bigger index, we need 3 vertex for a triangle but if j<i+2 we cant form a triangle
            
        res = float('inf') 
        # Initialize with infinity because we are looking for the minimum score. 
        # If we started with 0, the min() function would always return 0, 
        for k in range(i+1, j):
            res= min(res, values[i]*values[k]*values[j] + minTriangulationScore(i,k) + minTriangulationScore(k,j))
            # First, we form a triangle using vertices i, k, j.
            # This splits the current polygon into two smaller sub-polygons: (i..k) and (k..j).
            # We then recursively compute the minimum triangulation score for each of these two sub-polygons.
                
        # Finally, we add the score of the current triangle to the scores of the sub-polygons.
        return res
        
    #start from the vertex at index 0 and calculate to the last
    return minTriangulationScore(0, len(values) - 1)


values = [1,3,1,4,1,5]
print(minScoreTriangulation(values))