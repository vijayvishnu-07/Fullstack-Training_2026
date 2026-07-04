# Add your LeetCode solution here
class Solution:
    def minimumOperations(self, grid):
        ans = 0

        for j in range(len(grid[0])):     
            for i in range(1, len(grid)):  
                if grid[i][j] <= grid[i-1][j]:
                    need = grid[i-1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need

        return ans

