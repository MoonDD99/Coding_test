from collections import deque
# Enter your code here. Read input from STDIN. Print output to STDOUT
stack = deque() # (S, operations)

stdin = input().split()
n = int(stdin[0])
s = "" if len(stdin) == 1 else stdin[1]

stack.appendleft((s,0))

for index in range(n):
    operations = input().split()
    (s, operation) = stack[0]
    if operations[0] == "1":
        #append
        stack.appendleft((s+operations[1], 1))
    elif operations[0] == "2":
        #delete
        newS = s[:(len(s)-int(operations[1]))]
        stack.appendleft((newS,2))
    elif operations[0] == "3":
        #print
        print(s[int(operations[1])-1])
        stack.appendleft((s,3))
    else:
        (s,operation) = stack.popleft()
        while operation == 3:
            (s,operation) = stack.popleft()

        
        
    
    