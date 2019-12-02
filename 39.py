from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rt = []
        candidates.sort()

        def helper(candidates: List[int], target: int, index: int, comb: List[int]):
            if target == 0:
                rt.append(comb.copy())
                return
            elif target < candidates[index]:
                return
            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                helper(candidates, target - candidates[i], i, comb)
                comb.pop()

        helper(candidates, target, 0, [])
        return rt


# test = Solution.combinationSum(Solution, [2, 3, 6, 7], 7)
s = Solution()

print(s.combinationSum([2, 3, 6, 7], 7))
# print(test)
