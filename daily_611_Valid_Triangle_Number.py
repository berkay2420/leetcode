# Given an integer array nums, return the number of triplets chosen from the array that can make triangles 
# if we take them as side lengths of a triangle.

###################################
#### Example 1: ####

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
#   2,3,4 (using the first 2)
#   2,3,4 (using the second 2)
#   2,2,3
###################################


def triangleNumber(nums) -> int:
    nums.sort()
    counter = 0

    # start from the last item and go left, the number in index k is the longest edge
    # the last index for k is 2 because we are checking for triangles.
    for k in range(len(nums) - 1, 1, -1): 
        
        i = 0 # shortest edge
        j = k - 1 # the edge in the middle

        while i < j:
            if nums[i] + nums[j] > nums[k]:
                
                counter += (j - i) 
                # i is the shortest and j is just one lower then k (longest edge)
                # this means if this condition true it would be true for all the 
                # number between j and i also

                # nums[2,3,4,5,6,7,7,8,9] then nums[i]=2, nums[j]=8, nums[k]=9
                # if 2 + 8 > 9 this means this condition is also correct for every number between nums[i] and nums[j]
                # (we are already sorted the list before the for loop)
                
                j -= 1 # one more index to the left
            else:
                i += 1 # one more index to the right


    return counter

list1 = [2,2,3,4]
list2 = [4,2,3,4]

list1_triangle_count= triangleNumber(list1)
list2_triangle_count= triangleNumber(list2)

print(f"Total Valid Combination Count For {list1} is {list1_triangle_count}")
print(f"Total Valid Combination Count For {list2} is {list2_triangle_count}")