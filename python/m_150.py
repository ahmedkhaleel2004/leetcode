class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # neetcode solution without eval
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]

        # my solution beats 5%
        # stack = []

        # for i in tokens:
        #     stack.append(i)
        #     if stack and stack[-1] in ["*", "/", "+", "-"]:
        #         operator = stack.pop()
        #         second = stack.pop()
        #         first = stack.pop()
        #         stack.append(str(int(eval(first + operator + second))))

            
        # return int(stack[0])
