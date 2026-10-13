package java_lang;

import java.util.Arrays;

class Solution {
    public long maxAlternatingSum(int[] nums) {
        int minus = nums.length / 2;
        long result = 0;
        for (int i = 0; i < nums.length; i++) {
            nums[i] *= nums[i];
        }

        Arrays.sort(nums);

        for (int num: nums) {
            if (minus > 0) {
                result -= num;
                minus--;
            } else {
                result += num;
            }
        }
        return result;
    }
}

public class Problem3727 {
    public static void main(String[] args) {
        int[] nums = {-2,3,-3, 1,-1,2};
        var solution = new Solution();
        System.out.println(solution.maxAlternatingSum(nums));
    }
}
