# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

que = deque()
numQuery = int(input())

for query in range(numQuery):
    command = input().split()
    
    if command[0] == '1':
        que.append(int(command[1]))
    elif command[0] == '2':
        que.popleft()
    else:
        print(que[0])

    
    