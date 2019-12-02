from typing import List


#
#
# class Solution(object):
#     def splitArray(self, nums, m):
#         """
#         :type nums: List[int]
#         :type m: int
#         :rtype: int
#         """
#         def valid(mid):
#             cnt = 0
#             current = 0
#             for n in nums:
#                 current += n
#                 if current>mid:
#                     cnt += 1
#                     if cnt>=m:
#                         return False
#                     current = n
#             return True
#
#         l = max(nums)
#         h = sum(nums)
#
#         while l<h:
#             mid = l+(h-l)/2
#             if valid(mid):
#                 h = mid
#             else:
#                 l = mid+1
#         return l


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def cansplit(nums, m, target) -> bool:
            count, summation = 1, 0
            for num in nums:
                summation += num
                if summation > target:
                    if count >= m:
                        return False
                    summation = num
                    count += 1
            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) / 2
            if cansplit(nums, m, mid):
                r = mid
            else:
                l = mid + 1
        return int(r)


print(Solution.splitArray(Solution, [7, 2, 5, 10, 8], 2))
