from math import ceil

def failsolution(n, stations, w):
    answer = 0
    visited = [-1 for _ in range(n+1)]

    for center in stations:
        left = 1 if (center - w) < 0 else center - w
        right = n if (center + w) > n else center + w

        for index in range(left, right+1, 1):
            visited[index] = 1

    visited[0] = visited[1]

    count = 0
    for index in range(1, n+1):
        if visited[index-1] * visited[index] == 1:
            count += 1
        else : 
            answer += ceil(count/(w*2 +1))
            print("answer : " + str(answer))
            count = 1
        print("index : " + str(index) + " count : " + str(count))
    result = answer + ceil(count/(w*2 +1)) - len(stations)
    return 1 if result < 0 else result

def solution(n, stations, w):
    answer = 0

    index = 1
    for station in stations:
        count = max((station - w) - index, 0)
        answer += ceil(count/(w*2+1))
        index = station + w + 1

    if index <= n:
        answer += ceil((n - index + 1) / (w*2+1))
    return answer
N = 20
stations = [1,2,3,4]
W = 6
answer = solution1(N,stations,W)
print(answer)