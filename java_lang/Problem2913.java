package java_lang;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int left = 0;
        int right = 0;
        int num = 0;
        int result = 0;
        int leftValue = 0;
        int rightValue = 0;
        
        for (int len = 1; len <= nums.size(); len++) {
            Map<Integer, Integer> freq = new HashMap<>();
            left = 0;
            right = 0;
            while (right < nums.size()) {
                while ((right - left) + 1 < len) {
                    num = nums.get(right);
                    freq.put(num, freq.getOrDefault(nums, 0) + 1);
                    right++;
                }
                leftValue = nums.get(left);
                rightValue = nums.get(right);
                freq.put(rightValue, freq.get(rightValue + 1));
                System.out.print("[" + left + "," + right + "]: ");
                System.out.println(freq.size());
                result += freq.size();
                freq.put(leftValue, freq.get(leftValue - 1));
                if (freq.get(leftValue) == 0) {
                    System.out.println(freq.get(leftValue));
                    freq.remove(leftValue);
                }
                left++;
                right++;
            } 
        }
        return result;
    }
}

public class Problem2913 {
    public static void main(String[] args) {
        
    }
}
