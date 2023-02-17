from collections import deque
class Solution:
    def largestRectangleArea(heights):
        answer = []
        stacks = []
        stack = deque() #(height, width, size)
        for height in heights:
            if height == 0:
                stacks.append(stack)
                stacks.append(deque([(height,1,height)]))
                stack = deque()
            else:
                stack.append((height,1, height))
        stacks.append(stack)

        print(stacks)
        for stack in stacks:
            if len(stack) == 1:
                answer.append((stack[0])[2])
            elif len(stack) > 1:
                while len(stack) > 1:
                    bar1 = stack.popleft()
                    bar2 = stack.popleft()
                    mixBar = (min(bar1[0],bar2[0]), bar1[1]+1,(min(bar1[0],bar2[0]) * (bar1[1]+1)))
                    maxBar = max([bar1,bar2,mixBar],key = lambda x:x[2])
                    stack.appendleft(maxBar)
                    print(str(bar1) + ", " + str(bar2) + ",", str(mixBar))
                    print("stack : " + str(stack))
                answer.append((max([stack.popleft(),maxBar], key=lambda x:x[2]))[2])
        return max(answer)

    def largestRectangleArea1(heights):
        answer = []
        stack = deque()
        for height in heights:
            stack.append((height,1, height))
        print(stack)
        while len(stack) > 1:
            bar1 = stack.popleft()
            bar2 = stack.popleft()
            mixBar = (min(bar1[0],bar2[0]), bar1[1]+1,(min(bar1[0],bar2[0]) * (bar1[1]+1)))
            maxBar = max([bar1,bar2,mixBar],key = lambda x:x[2])
            if bar2[0] < bar1[0]:
                answer.append(maxBar[2])
                stack.appendleft(max([bar2,mixBar],key = lambda x:x[2]))
            else:
                stack.appendleft(maxBar)
            print(stack)
        answer.append((stack.popleft())[2])
        return max(answer)
    def largestRectangleArea2(heights):
        stack = deque()
        max = heights[0]
        for index in range(len(heights)):
            if len(stack) == 0:
                stack.appendleft(index)
            elif heights[index] >= heights[stack[0]] :
                stack.appendleft(index)
            else:
                while stack:
                    top = stack.popleft()
                    if (index-top) * heights[top] > max:
                        max = (index-top) * heights[top]
                    print("top : " + str(top) + " max : " + str(max))
                stack.appendleft(index)
        while stack:
            top = stack.popleft()
            if (len(heights)-top) * heights[top] > max:
                max = (len(heights) -top) * heights[top]
            print("top : " + str(top) + " max : " + str(max))
        return max

heights = [2,1,5,6,2,3]
answer = Solution.largestRectangleArea2(heights)
print(answer)