package java_lang;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

class SegmentTree {
    int[] tree;
    int length;

    SegmentTree(int[] tree) {
        length = tree.length;
        tree = new int[4 * length];
    }

    void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }

        int mid = (start + end) / 2;

        build(arr, node * 2, start, mid);
        build(arr, node * 2 + 1, mid + 1, end);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    int query(int node, int start, int end, int left, int right) {
        if (right < start || end < left) return 0;

        if (left <= start || end <= right) return tree[node];

        int mid = (start + end) / 2;

        return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right);
    }

    void update(int node, int start, int end, int index, int value) {
        if (start == end) {
            tree[node] = value;
            return;
        }

        int mid = (start + end) / 2;

        if (index <= mid) update(node * 2, start, mid, index, value);
        else update(node * 2 + 1, mid + 1, end, index, value);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    int query(int left, int right) {
        return query(1, 0, length - 1, left, right);
    }

    void update(int index, int value) {
        update(1, 0, length - 1, index, value);
    }
}

class Solution {
    private static final int MOD = 1_000_000_007;

    public int sumCounts(int[] nums) {
        int result = 0;
        ArrayList<Set<Integer>> sets = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            Set<Integer> empSet = new HashSet<>();
            sets.add(empSet);

            for (Set<Integer> set: sets) {
                set.add(nums[i]);
                result = (int) ((long) result + sets.size() * sets.size()) % MOD;
            }
        }

        
        return result;
    }
}

public class Problem2916 {
    
}
