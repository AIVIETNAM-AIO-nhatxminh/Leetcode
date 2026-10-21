package java_lang;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final double MOD = 1000_000_007f;

    public double digitBreakdown(int num) {
        double result = 0;

        while (num >= 1) {
            result += num % 10;
            num /= 10;
        }

        return result;
    }

    public int minSwaps(int[] nums) {
        Map<Double, Integer> indexMap = new HashMap<>();
        int result = 0;
        
        double[] digitSum = new double[nums.length];

        for (int i = 0; i < nums.length; i++) {
            digitSum[i] = digitBreakdown(nums[i]) + ( (double) nums[i] / MOD);
        }

        for (int i = 0; i < digitSum.length; i++) {
            indexMap.put(digitSum[i], i);
        }

        System.out.println(indexMap.toString());

        Arrays.sort(digitSum);

        for (int i = 0; i < digitSum.length; i++) {
            while (indexMap.get(digitSum[i]) != i) {
                int idx = indexMap.get(digitSum[i]);
                double temp = digitSum[idx];
                digitSum[idx] = digitSum[i];
                digitSum[i] = temp;
                result++;
            }
        }
        return result;
    }
}

public class Problem3551 {
    public static void main(String[] args) {
        int[] nums = {18,43,34,16};
        var solution = new Solution();
        System.out.println(solution.minSwaps(nums));
    }
}
