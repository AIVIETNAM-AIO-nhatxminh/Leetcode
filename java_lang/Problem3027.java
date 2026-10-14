package java_lang;

class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (sum > num * 9) {
            return "";
        }

        StringBuilder result = new StringBuilder();
        result.append("9".repeat(sum / 9));

        sum %= 9;

        if (sum > 0) result.append(sum);
        result.append("0".repeat(num - result.length()));

        return result.toString();
    }
}

public class Problem3027 {
    public static void main(String[] args) {
        var num = 2;
        var sum = 10;
        var solution = new Solution();
        System.out.println(solution.maxSumOfSquares(num, sum));
    }
}
