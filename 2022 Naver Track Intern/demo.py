def solution(A):
    isThere = [False] * 1000000
    for element in A:
        if element >= 1 : 
            isThere[element] = True
    for index in range(1,len(isThere),1) :
        if isThere[index] != True:
            return index

input = [1, 3, 6, 4, 1, 2]
output = solution(input)
print(output)