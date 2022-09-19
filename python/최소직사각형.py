def solution(sizes):
    result = set()
    for size in sizes:
        width = size[0]
        height = size[1]
        for compareSize in sizes:
            if (compareSize[0] > width or compareSize[1] > height) or (compareSize[0] > height or compareSize[1] > width) :
                continue
        result.update([width*height])
    print(result)
    return min(result)

sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
sizes.sort()
print(sizes)
#answer = solution(sizes)
#print(answer)