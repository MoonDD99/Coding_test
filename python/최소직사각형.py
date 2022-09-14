def solution(sizes):
    result = set()
    for size in sizes:
        width = size[0]
        height = size[1]
        for compareSize in sizes:
            if not(compareSize[0] == width and compareSize[1] == height) and ((compareSize[0] <= width and compareSize[1] <= height) or (compareSize[0] <= height and compareSize[1] <= width)) :
                print(size)
                result.update([width*height])
        
    return min(result)

sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
answer = solution(sizes)
print(answer)