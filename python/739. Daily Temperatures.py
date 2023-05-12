from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                preIndex = stack.pop()
                result[preIndex] = index - preIndex
            stack.append(index)
        
        return result

            
