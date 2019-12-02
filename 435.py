from typing import List
class Solution:
    # greed： 根据一个维度的大小顺序循环，会简化问题、降维。本题从先排序左边的大小，只需要比较新的间距的左边界是不是比维护的有界小
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0])
        rt = 0
        right = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < right:
                rt += 1
                right = min(right, interval[1])
            else:
                right = interval[1]
        return rt


# test = Solution.eraseOverlapIntervals(Solution, [[1, 2], [2, 3], [3, 4], [1, 3]])

test = Solution.eraseOverlapIntervals(Solution, [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]])
print('res:', test)
