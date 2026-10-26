package java_lang;


class Solution {
    public long dfs(int[][] grid, boolean[][] visited, int row, int col, int width, int height) {
        long result = grid[row][col];
        visited[row][col] = true;

        if (row > 0 && !visited[row - 1][col] && grid[row - 1][col] != 0) {
            result += dfs(grid, visited, row - 1, col, width, height);
        }

        if (col > 0 && !visited[row][col - 1] && grid[row][col - 1] != 0) {
            result += dfs(grid, visited, row, col - 1, width, height);
        }

        if (row < height - 1 && !visited[row + 1][col] && grid[row + 1][col] != 0) {
            result += dfs(grid, visited, row + 1, col, width, height);
        }


        if (col < width - 1 && !visited[row][col + 1] && grid[row][col + 1] != 0) {
            result += dfs(grid, visited, row, col + 1, width, height);
        }

        return result;
    }

    public int countIslands(int[][] grid, int k) {
        int result = 0;
        long currSum = 0;
        int height = grid.length;
        int width = grid[0].length;
        boolean[][] visited = new boolean[height][width];

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (!visited[i][j]) {
                    if (grid[i][j] == 0) {
                        visited[i][j] = true;
                        continue;
                    }
                    currSum = dfs(grid, visited, i, j, width, height);
                    System.out.println(currSum);

                    if (currSum % k == 0) {
                        System.out.println(currSum);
                        result += 1;
                        currSum = 0;
                    }
                }
            }
        }
        return result;
    }
}

public class Problem3619 {
    public static void main(String[] args) {
        int[][] grid = {{3,0,3,0},{0,3,0,3},{3,0,3,0}};
        var solution = new Solution();

        System.out.println(solution.countIslands(grid, 3));
    }
}
