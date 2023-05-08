from collections import deque
def search(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
    return 1 if len(stack) == 0 else 0
                
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        answer += search(s)
        s = s[1:] + s[:1]
            
    return answer