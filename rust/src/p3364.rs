pub struct Solution;

impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        let mut result = i32::MAX;
        let mut sum: i32;
        let mut left: usize;
        let mut has_result: bool = false;

        for length in l..=r {
            sum = 0;
            left = 0;
            for (right, num) in nums.iter().enumerate()  {
                sum += num;
                println!("{}", sum);
                if (right - left + 1) < length as usize {
                    continue;
                }
                if sum > 0 && sum < result {
                    has_result = true;
                    result = sum;
                }
                sum -= nums[left];
                left += 1;
            }
        }

        return if has_result {result} else {-1};
    }
}