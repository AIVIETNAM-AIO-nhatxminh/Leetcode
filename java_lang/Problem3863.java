package java_lang;

class Solution {
    public int minOperations(String s) {
        int length = s.length();
        int[] alphabet = new int[length];
        int prev = (int) s.charAt(0);
        int smallest = prev;
        int highest = smallest;
        int[] count = new int[26];
        boolean sorted = true;

        if (length == 1) return 0;

        if (length == 2) {
            if (s.charAt(0) < s.charAt(1)) {
                return 0;
            } else {
                return -1;
            }
        } 

        for (int i = 0; i < length; i++) {
            int unicode = (int) s.charAt(i);
            alphabet[i] = unicode;
            count[unicode - 97] += 1;

            if (unicode < smallest) {
                smallest = unicode;
            }

            if (unicode > highest) {
                highest = unicode;
            }

            if (unicode < prev) {
                sorted = false;
            } 

            prev = unicode;
        }

        if (!sorted) {
            if (alphabet[0] == highest && alphabet[length] == smallest) {
                if (count[highest] > 1 || count[smallest] > 1) {
                    return 2;
                } else {
                    return 3;
                }
            } else if (alphabet[0] == smallest || alphabet[length] == highest) {
                return 1;
            } else {
                return 2;
            }
        }
        return 0;
    }
}

public class Problem3863 {
    
}
