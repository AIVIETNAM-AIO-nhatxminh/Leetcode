package java_lang;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        ArrayList<Integer> result = new ArrayList<>();
        int smaller = 0;
        int equal = 0;

        for (int num: nums) {
            if (num == target) {
                equal++;
            } else if (num < target) {
                smaller++;
            }
        }

        for (int i = 0; i < equal; i++) {
            result.add(i + smaller);
        }

        return result;
    }
}

public class Problem2089 {
    
}
