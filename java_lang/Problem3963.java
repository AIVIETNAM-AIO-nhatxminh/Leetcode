package java_lang;

class Solution {
    public String[] createGrid(int m, int n) {
        String[] result = new String[m];

        String first = ".".repeat(n);
        String rest  = "#".repeat(n - 1) + ".";  

        result[0] = first;
        for (int i = 1; i < m; i++) {
            result[i] = rest;                   
        }
        return result;
    }
}

public class Problem3963 {
    
}
