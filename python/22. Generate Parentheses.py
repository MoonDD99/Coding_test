from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] 
    
        def dfs(pairs: list):
            if len(pairs) == n * 2:
                stack = deque([])
                if pairs[0] != "(":
                    return
                else :
                    for pair in pairs:
                        if len(stack) == 0:
                            stack.append
                        if pair == "(":
                            stack.append(pair)
                        else:
                            if len(stack) != 0 and stack[-1] == "(":
                                stack.pop()
                            else:
                                return
                    if len(stack) == 0 :
                        result.append(''.join(pairs))
                
                
            else:
                dfs(list(pairs) + ["("])
                dfs(list(pairs) + [")"])
        
        pairs = ["("]
        dfs(pairs)
        return result
