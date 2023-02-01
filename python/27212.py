import sys

scores = []

N, M, C = map(int, sys.stdin.readline().rstrip().split())
for i in range(C):
    scores.append(list(map(int, sys.stdin.readline().rstrip().split())))
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

satisfy = [[0]*M for _ in range(N)]

for n in range(N):
    for m in range(M):
        satisfy[n][m] = scores[A[n]-1][B[m]-1]

dp = [[0]*(M+1) for _ in range(N+1)]

for n in range(1,N+1):
    for m in range(1,M+1):
        dp[n][m] = max((dp[n-1][m-1]+satisfy[n-1][m-1]), dp[n-1][m], dp[n][m-1])

print(dp[-1][-1])