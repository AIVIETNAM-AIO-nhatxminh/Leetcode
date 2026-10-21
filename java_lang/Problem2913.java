package java_lang;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int result = 0;
        int count = 0;

        for (int i = 0; i < nums.size(); i++) {
            Set<Integer> unique = new HashSet<>();
            count = 0;
            
            for (int j = i; j < nums.size(); j++) {
                int num = nums.get(j);

                if (!unique.contains(num)) {
                    unique.add(num);
                    count++;
                }
                result += count * count;
            }
        }
        return result;
    }
}

public class Problem2913 {
    public static void main(String[] args) {
        
    }
}
