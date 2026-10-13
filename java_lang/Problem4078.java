package java_lang;

import java.util.HashSet;
import java.util.Set;

class Solution {
    private static int length = 46;
    private static int[] fibonacci = new int[length];
    private static Set<Integer> threeSum = new HashSet<>();

    static {
        fibonacci[0] = 0;
        fibonacci[1] = 1;

        for (int i = 2; i < length; i++) {
            int prev1 = fibonacci[i - 1];
            int prev2 = fibonacci[i - 2];
            int curr = prev1 + prev2;
            fibonacci[i] = curr;
            if (i >= 2) {
                threeSum.add(curr + prev1 + prev2);
            }
        }
    }

    public boolean threeFibonacciSum(int n) {
        if (threeSum.contains(n)) {
            return true;
        } else {
            return false;
        }
    }
}

public class Problem4078 {
    public static void main(String[] args) {
        var n = 16;
        var solution = new Solution();
        System.out.println(solution.threeFibonacciSum(n));
    }
}
