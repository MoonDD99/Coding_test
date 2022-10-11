def solution(n, costs):
    weight = 0
    costs.sort(key = lambda x: x[2])
    connectSet = set([costs[0][0]])

    while len(connectSet) != n :
        for cost in costs:
            if cost[0] in connectSet and cost[1] in connectSet:
                continue
            if cost[0] in connectSet or cost[1] in connectSet:
                weight += cost[2]
                connectSet.update([cost[0], cost[1]])
                break
    return weight


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
result = solution(4, costs)
print(result)