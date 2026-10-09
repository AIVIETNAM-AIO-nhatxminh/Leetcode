package java_lang;

import java.lang.Math;

class Solution {
    public int minInsertions(String s) {
        var result = 0;
        var count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                if (count >= 0) {
                    if (count % 2 == 0) {
                        count += 2;
                    } else {
                        result += 1;
                        count += 1;
                    }
                } else {
                    result += Math.ceilDiv(-(count), 2);
                    count += Math.ceilDiv(-(count), 2) * 2;
                    if (count % 2 != 0) {
                        count -= 1;
                        result += 1;
                    } 
                    count += 2;
                }
            } else if (s.charAt(i) == ')') {
                count--;
            }
        }

        while (count != 0) {
            if (count > 0) {
                count--;
                result++;
            } else {
                count += 2;
                result++;
            }
        }
        return result;
    }
}

public class Problem1541 {
    public static void main(String[] args) {
        var solution = new Solution();
        var s = "()()))";
        System.out.println(solution.minInsertions(s));
    }
}
