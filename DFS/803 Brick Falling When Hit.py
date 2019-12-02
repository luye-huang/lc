from typing import List

# 先要倒掉的砖块抠掉，然后从根部dfs尽量连接，然后按照抠掉顺序反序贴上
# 为什么要倒序？正序处理前面贴上去的砖会覆盖后面要贴上去的
# 倒序时注意判断是否和根部相连 isConnected， 否则就是属于前面的砖已经贴过的情况

# https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        h, w = len(grid), len(grid[0])
        ret = [0] * len(hits)

        def isConnected(i, j) -> bool:
            return i == 0 or any(0 <= y < h and 0 <= x < w and grid[y][x] == 2 for y, x in
                                  [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        def dfs(i, j) -> int:
            if not (0 <= i < h and 0 <= j < w) or grid[i][j] != 1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += sum(dfs(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
            return ret

        for i, j in hits:
            grid[i][j] -= 1

        for i in range(w):
            dfs(0, i)

        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and isConnected(i, j):
                ret[k] = dfs(i, j) - 1

        return ret






# print(Solution.hitBricks(Solution, [[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]), '0,3,0')
# print(Solution.hitBricks(Solution, [[1, 1, 0, 1, 0],
#                                     [1, 1, 0, 1, 1],
#                                     [0, 0, 0, 1, 1],
#                                     [0, 0, 0, 1, 0],
#                                     [0, 0, 0, 0, 0],
#                                     [0, 0, 0, 0, 0]]
#                          , [[5, 1], [1, 3]]), '0,4')
#
# print(Solution.hitBricks(Solution, [[0, 1, 1, 1, 1],
#                                     [1, 1, 1, 1, 0],
#                                     [1, 1, 1, 1, 0],
#                                     [0, 0, 1, 1, 0], [0, 0, 1, 0, 0],
#                                     [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
#                          [[6, 0], [1, 0], [4, 3], [1, 2], [7, 1], [6, 3], [5, 2], [5, 1], [2, 4], [4, 4], [7, 3]]),
#       '全为0')
# print(Solution.hitBricks(Solution, [[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]]), '0,0,1,0')
# print(Solution.hitBricks(Solution, [[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]), '2')
# print(Solution.hitBricks(Solution, [[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]), '0,0')
print(Solution.hitBricks(Solution, [[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]), '1,0,1,0,0')
