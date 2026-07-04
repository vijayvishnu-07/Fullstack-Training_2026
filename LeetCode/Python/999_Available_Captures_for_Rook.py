# Add your LeetCode solution here
class Solution(object):
    def numRookCaptures(self, board):
        count = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':

                    for u in range(i - 1, -1, -1):
                        if board[u][j] == 'B':
                            break
                        if board[u][j] == 'p':
                            count += 1
                            break

                    for d in range(i + 1, 8):
                        if board[d][j] == 'B':
                            break
                        if board[d][j] == 'p':
                            count += 1
                            break

                    for l in range(j - 1, -1, -1):
                        if board[i][l] == 'B':
                            break
                        if board[i][l] == 'p':
                            count += 1
                            break

                    for r in range(j + 1, 8):
                        if board[i][r] == 'B':
                            break
                        if board[i][r] == 'p':
                            count += 1
                            break

                    return count