def solution(skill, skill_trees):
    #score : 28.6 / 100.0
    """
    C -> B -> D 일 경우 CB만 진행되어도 괜찮다.
    그래서 뒤에서 검사하는 방식은 옳지 않다.
    """
    answer = 0
    skill_stack = list(skill)

    for tree in skill_trees:
        stack = skill_stack
        print("tree: ",tree)
        #tree 문자열을 뒤에서부터 검사
        for index in range(len(tree)-1,-1,-1):
            print("index : ", index)
            print("tree[index] : ", tree[index])
            print("stack[-1:] : " , stack[-1:] )
            if len(stack) == 0:
                answer += 1
                break
            if tree[index] == stack[-1]:
                stack.pop()   
        
    return answer

def solution1(skill, skill_trees):
    #score : 100.0 / 100.0
    answer = 0
    
    for tree in skill_trees:
        flag = True
        skill_stack = list(skill)
        for c in tree:
            if c in skill:
                if c != skill_stack.pop(0):
                    flag = False
                    break
        if flag :
            answer += 1

    return answer   


from collections import deque
def solution2(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        treeDeque = deque(skill)
        for char in tree:
            if len(treeDeque) == 0:
                break
            skillChar = treeDeque.popleft()
            if skillChar != char:
                treeDeque.appendleft(skillChar)
            print(treeDeque)
        if len(treeDeque) <= 1:
            answer += 1
    return answer


skill = "CBD"
skill_tress = ["BDA", "BACDE", "CBADF", "AECB"]
#result = solution1(skill, skill_tress)
result = solution2(skill, skill_tress)
print(result)
