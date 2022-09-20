def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size[0],size[1]))
        height.append(min(size[0],size[1]))
    return max(width) * max(height)

#sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
#sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
answer = solution(sizes)
print(answer)