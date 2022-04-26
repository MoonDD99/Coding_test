def solution(N, road, K):
    answer = 0
    times = dict() 

    while len(road) > 0:
        current_road = road.pop(0)
        if current_road[0] == 1:
            if times.get(current_road[1]):
                times[current_road[1]] = min(times[current_road[1]],current_road[2])
            else:
                times[current_road[1]] = current_road[2]
        else:
            if times.get(current_road[0]):
                times[current_road[1]] = times[current_road[0]] + current_road[2]
            else:
                road.append(current_road)
                
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
result = solution(N,road,K)
print(result)