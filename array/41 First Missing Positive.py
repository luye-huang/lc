from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [num for num in range(len(nums) + 1)]
        for num in nums:
            if num <= 0:
                continue
            try:
                arr[num] = 0
            except Exception:
                pass
        for num in arr:
            if num != 0:
                return num
        else:
            return len(nums) + 1

print(Solution.firstMissingPositive(Solution, [-1, -2]))
print(Solution.firstMissingPositive(Solution, [0, 2, 99]))
print(Solution.firstMissingPositive(Solution, [3, 4, -1, 1]))
print(Solution.firstMissingPositive(Solution, [3, 4, 2, 1]))
