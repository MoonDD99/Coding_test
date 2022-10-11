def solution(n, losts, reserves):
    isExist = set()
    losts.sort()
    reserves.sort()
    for reserve in reserves:
        if reserve in losts:
            isExist.add(reserve)
            continue
        if reserve - 1 in losts and reserve - 1 not in isExist:
            isExist.add(reserve -1)
        elif reserve + 1 in losts and reserve + 1 not in isExist:
            isExist.add(reserve+1)
    return n- len(losts) + len(isExist)



n = 5
losts = [2, 4]
reserves = [1, 3, 5]

reserves = 	[3]

n = 3
losts = [3]
reserves = [1]
answer = solution(n, losts, reserves)
print(answer)