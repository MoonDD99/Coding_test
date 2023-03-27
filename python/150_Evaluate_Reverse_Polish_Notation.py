from collections import deque
import math
class Solution:
    def is_digit(token):
        try:
            result = float(token)
            return True
        except ValueError:
            return False
    def evalRPN(tokens):
        stack = deque()
        result = 0
        for token in tokens:
            print("token : " + str(token))
            print("stack : " + str(stack))
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
                    result = math.floor(num1/num2)
                stack.append(result)
        return result

input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = Solution.evalRPN(input)
print(result)