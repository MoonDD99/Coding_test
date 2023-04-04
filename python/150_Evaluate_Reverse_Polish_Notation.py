from collections import deque
import math
class Solution:
    def is_digit(token):
        try:
            result = float(token)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens):
        if len(tokens) == 1:
            return int(tokens[0])
        stack = deque()
        result = 0
        for token in tokens:
            #print("token : " + str(token))
            if Solution.is_digit(token):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    result = (num1 + num2)
                elif token == "-":
                    result = (num1 - num2)
                elif token == "*":
                    result = (num1 * num2)
                else:
                    result = math.trunc(num1/num2)
                stack.append(result)
            #print("stack : " + str(stack))
        return result
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == "+":
                num1 = stack.popleft()
                num2 = stack.popleft()
                stack.appendleft(num1 + num2)
            elif token == "-":
                num1 = stack.popleft()
                num2 = stack.popleft()
                stack.appendleft(num2 - num1)
            elif token == "*":
                num1 = stack.popleft()
                num2 = stack.popleft()
                stack.appendleft(int(num1 * num2))
            elif token == "/":
                num1 = stack.popleft()
                num2 = stack.popleft()
                stack.appendleft(int(num2 / num1))
            else:
                stack.appendleft(int(token))
            #print("token : " + token)
            #print("stack : " + str(stack))
        return stack[0]

