from typing import List
import bisect


class Solution:
    # 整体思路：
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        length = [len(nums1), len(nums2)]
        stack, ret, pos, count = [], [0] * k, [num for num in range(k)], 0
        head0, head1, tail0, tail1 = [0] * length[0], [0] * length[1], [k] * length[0], [k] * length[1]
        head = 0
        for i in range(length[0]):
            value = nums1[i]
            elements = length[1] + length[0] - i - 1
            head0[i] = max(k - elements - 1, 0)
            elements = length[1] + i
            tail0[i] = elements
            stack.append({'value': value, 'arr': head, 'index': i})
            for j in range(len(stack) - 2, -1, -1):
                if stack[j]['value'] < stack[j + 1]['value']:
                    stack[j], stack[j + 1] = stack[j + 1], stack[j]
                else:
                    break
        head = 1
        for i in range(length[1]):
            value = nums2[i]
            elements = length[0] + length[1] - i - 1
            head1[i] = max(k - elements - 1, 0)
            elements = length[0] + i
            tail1[i] = elements
            stack.append({'value': value, 'arr': head, 'index': i})
            for j in range(len(stack) - 2, -1, -1):
                if stack[j]['value'] < stack[j + 1]['value']:
                    stack[j], stack[j + 1] = stack[j + 1], stack[j]
                else:
                    break

        for val in stack:
            is_num1, idx_val, head, tail = val['arr'] == 0, val['index'], 0, k
            if is_num1:
                head, tail = head0[idx_val], tail0[idx_val]
            else:
                head, tail = head1[idx_val], tail1[idx_val]
            if head > tail:
                continue
            for i, v in enumerate(pos):
                if v >= head and v <= tail:
                    ret[pos.pop(i)] = val['value']
                    count += 1
                    if count == k:
                        return ret
                    if is_num1:
                        tail0[:idx_val] = [v - 1] * idx_val
                    else:
                        tail1[:idx_val] = [v - 1] * idx_val
                    break

        return ret


# print(Solution.maxNumber(Solution, [3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
print(Solution.maxNumber(Solution, [6, 7], [6, 0, 4], 5))
