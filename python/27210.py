import sys
n = int(sys.stdin.readline().rstrip())
stones = list(map(int, sys.stdin.readline().rstrip().split()))

sumList = [0]
sum = 0

for stone in stones:
    if stone == 1:
        sum += 1
    else :
        sum -= 1
    sumList.append(sum)
print(abs(max(sumList) - min(sumList)))
