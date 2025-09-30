# You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).
# The triangular sum of nums is the value of the only element present in nums after 
# the following process terminates:

# Let nums comprise of n elements. If n == 1, end the process. 
# Otherwise, create a new 0-indexed integer array newNums of length n - 1.
# For each index i, where 0 <= i < n - 1, 
# assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the triangular sum of nums.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: 8
# Explanation:
#     The above diagram depicts the process from which we obtain the triangular sum of the array.

# Example 2:
# Input: nums = [5]
# Output: 5
# Explanation:
# Since there is only one element in nums, the triangular sum is the value of that element itself.


def triangularSum(nums):
    while(len(nums) > 1 ):
        new_nums = []
        for i in range(len(nums) - 1):
            new_nums.append((nums[i] + nums[i+1]) % 10)
        nums = new_nums
    return nums[0]

list1 = [1,2,3,4,5]
list2 = [8]

print(f"Triangle sum of {list1} list is: {triangularSum(list1)} \n")
print(f"Triangle sum of {list2} list is: {triangularSum(list2)} \n")

###### another (worse) solution ########
# class Solution:
#     def triangularSum(self, nums: List[int]) -> int:
#         def newNums(nums):
#             new_nums = []
#             for i in range(0, len(nums) - 1, 1):
#                 new_nums.append((nums[i] + nums[i+1]) % 10)
            
#             return new_nums

#         def findTriangularSum(nums):
#             new_nums = nums
#             while len(new_nums) > 1:
#                 new_nums = newNums(new_nums)
#             return new_nums

#         return findTriangularSum(nums)[0]    