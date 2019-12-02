
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 使用一个栈收集s的index
        stack = []
        for i, v in enumerate(s):
            # 如果栈头为（ 并且新元素为），则去栈头；否则入栈
            if v == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        ret = 0
        if len(stack) == 0:
            return len(s)
        if stack[0] != 0:
            stack.insert(0, -1)
        if stack[-1] != len(s) - 1:
            stack.append(len(s))
        # 栈中的index最大差值既是结果
        for i in range(1, len(stack)):
            ret = max(ret, stack[i] - stack[i - 1])
        return max(ret - 1, 0)


print(Solution.longestValidParentheses(Solution, "()(())"))
print(Solution.longestValidParentheses(Solution, "()"))
print(Solution.longestValidParentheses(Solution, "(()"))
print(Solution.longestValidParentheses(Solution, ")()())"))
