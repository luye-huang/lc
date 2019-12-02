from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        if len(nums) < 3:
            return map(list, ret)
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if v > 0:
                return map(list, ret)
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            target = -v
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target_ = nums[l] + nums[r]
                if target_ == target:
                    ret.add((v, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif target_ < target:
                    l += 1
                else:
                    r -= 1
        return map(list, ret)


print(Solution.threeSum(Solution, [-1, 0, 1, 2, -1, -4]))
print(Solution.threeSum(Solution, [0, 0, 0]))
