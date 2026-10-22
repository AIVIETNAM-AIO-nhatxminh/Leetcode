package java_lang;

class Solution {
    public int withinRange(int num, int range) {
        if (num >= range) {
            return num - range;
        } else if (num < 0) {
            return range + num;
        } else {
            return num;
        }
    }

    public int minOperations(int[] nums) {
        int zeroPos = 0;
        int prev = 0;
        int curr = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeroPos = i;
            }
        }

        prev = nums[zeroPos];
        for (int i = 1; i < nums.length; i++) {
            curr = nums[withinRange(zeroPos + i, nums.length)];
            if (curr - prev != 1) {
                break;
            }
            prev = curr;
            if (i == nums.length - 1) {
                return Math.min(zeroPos, 3 + (nums.length - 1 - zeroPos));
            }
        }

        prev = nums[zeroPos];
        for (int i = 1; i < nums.length; i++) {
            curr = nums[withinRange(zeroPos - i, nums.length)];
            if (curr - prev != 1) {
                break;
            }
            prev = curr;
            if (i == nums.length - 1) {
                if (zeroPos == 0) {
                    return 2;
                } else if (zeroPos == nums.length - 1) {
                    return 1;
                } else {
                    return Math.min((nums.length - 1) - zeroPos + 1, zeroPos + 2);
                }
            }
        }

        return -1;    
    }
}

public class Problem3942 {
    public static void main(String[] args) {
        int[] nums = {0,2,1};
        var solution = new Solution();
        System.out.println(solution.minOperations(nums));
    }
}
