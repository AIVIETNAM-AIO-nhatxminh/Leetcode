mod p3364;

fn main() {
    let nums: Vec<i32> = vec![3, -2, 1, 4];let l: i32 = 2;let r: i32 = 3;
    dbg!(p3364::Solution::minimum_sum_subarray(nums, l, r));
}
