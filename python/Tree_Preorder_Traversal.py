from collections import deque
def preOrder(root):
    #Write your code here
    answer = ""
    stack = deque([root])
    
    while stack:
        node = stack.popleft()
        answer += str(node.info) + " "
        if node.right != None:
            stack.appendleft(node.right)
        if node.left != None:
            stack.appendleft(node.left)

    print(answer)

from collections import deque
def preOrder(root):
    #Write your code here
    if root == None:
        return
    print(root.info, end = " ")
    
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)