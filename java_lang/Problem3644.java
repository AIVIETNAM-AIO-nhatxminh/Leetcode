package java_lang;

class Solution {
    public int sortPermutation(int[] nums) {
        int result = (1<<17) - 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) result &= nums[i];
        }
        return (result != (1<<17) - 1) ? result : 0;
    }
}

public class Problem3644 {
    public static void main(String[] args) {
        int[] nums = {0,1,2,3,7,6,4,5};
        var solution = new Solution();
        System.out.println(solution.sortPermutation(nums));
    }
}
