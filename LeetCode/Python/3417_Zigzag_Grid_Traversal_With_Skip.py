# Add your LeetCode solution here
class Solution(object):
    def zigzagTraversal(self, grid):
        res = []
        row = 0
        z = 0

        for l in grid:

            if row % 2 == 0:
                for i in range(len(l)):
                    if z == 0:
                        res.append(l[i])
                        z = 1
                    else:
                        z = 0

            else:
                for i in range(len(l) - 1, -1, -1):
                    if z == 0:
                        res.append(l[i])
                        z = 1
                    else:
                        z = 0

            row += 1

        return res