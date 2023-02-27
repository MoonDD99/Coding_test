from collections import deque
def isBalanced(s):
    # Write your code here
    stack = deque()
    
    for element in s:
        if element == "{" or element == "[" or element == "(":
            stack.appendleft(element)
        else:
            if len(stack) == 0:
                return "NO"
            elif element == "}" and stack[0] == "{":
                stack.popleft()
            elif element == "]" and stack[0] == "[":
                stack.popleft()
            elif element == ")" and stack[0] == "(":
                stack.popleft()
            else:
                return "NO"
        print(stack)
    if len(stack) == 0:
        return "YES"
    return "NO"

s = "}][}}(}][))]"
answer = isBalanced(s)
print(answer)