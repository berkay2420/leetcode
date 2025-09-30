import java.util.Arrays;

class Solution {
    public int triangularSum(int[] nums) {
        while (nums.length > 1) {
            int[] newNums = new int[nums.length - 1];
            for (int i = 0; i < nums.length - 1; i++) {
                newNums[i] = (nums[i] + nums[i + 1]) % 10;
            }
            nums = newNums; 
        }
        return nums[0];
    }


    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] list1 = {1, 2, 3, 4, 5};
        int[] list2 = {8};
        System.out.println("Triangle sum of list1: " + sol.triangularSum(list1));
        System.out.println("Triangle sum of list2: " + sol.triangularSum(list2));
    }
}
