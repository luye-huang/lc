from typing import List


# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         length = len(positions)
#         heights = [x[1] for x in positions]
#         ret = heights.copy()
#         for i in range(1, length):
#             up = positions[i]
#             height = 0
#             for j in range(i):
#                 down = positions[j]
#                 if not (up[0] + up[1] <= down[0] or down[0] + down[1] <= up[0]):
#                     height = max(height, heights[j])
#             heights[i] += height
#             ret[i] = max(ret[i - 1], heights[i])
#         return ret


# binary search
# import bisect
# class Solution(object):
#     def fallingSquares(self, positions):
#         axis = [0, float('inf')]
#         heights = [0, 0]
#         an = [0]
#         for left, length in positions:
#             right = left + length
#             idl = bisect.bisect_right(axis, left)
#             idr = bisect.bisect_left(axis, right)
#
#             h = max(heights[idl - 1: idr]) + length
#
#             axis[idl: idr] = [left, right]
#             heights[idl: idr] = [h, heights[idr - 1]]
#             an.append(max(an[-1], h))
#
#         return an[1:]


class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # compress positions into consecutive indices
        all_pos = set()
        for p in positions:
            all_pos.add(p[0])
            all_pos.add(p[0] + p[1])

        pos_ind = {}
        for i, pos in enumerate(sorted(all_pos)):
            pos_ind[pos] = i

        n = len(pos_ind)
        segtree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def _insert(left, right, h, root, start, end):
            if lazy[root] != 0:
                if start != end:
                    lazy[root * 2] = max(lazy[root * 2], lazy[root])
                    lazy[root * 2 + 1] = max(lazy[root * 2 + 1], lazy[root])
                segtree[root] = max(segtree[root], lazy[root])
                lazy[root] = 0

            if left > end or right < start:
                return

            if start == end:
                segtree[root] = max(segtree[root], h)
                return

            if left <= start and right >= end:
                segtree[root] = max(segtree[root], h)
                lazy[root * 2] = max(lazy[root * 2], h)
                lazy[root * 2 + 1] = max(lazy[root * 2 + 1], h)
                return

            mid = (start + end) // 2
            _insert(left, right, h, root * 2, start, mid)
            _insert(left, right, h, root * 2 + 1, mid + 1, end)
            segtree[root] = max(segtree[2 * root], segtree[2 * root + 1], h)
            return

        def _query(left, right, root, start, end):
            if lazy[root] != 0:
                if start != end:
                    lazy[root * 2] = max(lazy[root * 2], lazy[root])
                    lazy[root * 2 + 1] = max(lazy[root * 2 + 1], lazy[root])
                segtree[root] = max(segtree[root], lazy[root])
                lazy[root] = 0

            if left > end or right < start:
                return 0

            if start == end:
                return segtree[root]

            if left <= start and right >= end:
                return segtree[root]

            mid = (start + end) // 2
            return max(_query(left, right, root * 2, start, mid), _query(left, right, root * 2 + 1, mid + 1, end))

        def insert(left, right, h):
            _insert(left, right, h, 1, 0, n - 1)

        def query(left, right):
            return _query(left, right, 1, 0, n - 1)

        res = []
        accu_max = 0
        for p in positions:
            left_raw, h = p
            right_raw = left_raw + h
            left = pos_ind[left_raw]
            right = pos_ind[right_raw] - 1
            cur_max = query(left, right)
            new_max = cur_max + h
            accu_max = max(accu_max, new_max)
            res.append(accu_max)
            insert(left, right, new_max)
            print('segtree:', segtree)
            print('segtree')
        return res


print(Solution.fallingSquares(Solution, [[2, 1], [2, 9], [1, 8]]))
print(Solution.fallingSquares(Solution, [[2, 1], [1, 1], [1, 8]]))
print(Solution.fallingSquares(Solution, [[1, 2], [2, 3], [6, 1]]))
