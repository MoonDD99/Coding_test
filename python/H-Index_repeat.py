def solution(citations):
    citations.sort()
    lenCitations = len(citations)
    for h in range(lenCitations):
        if citations[h] >= lenCitations - h:
            return lenCitations - h
    return 0

def failSolution(citations):
    sortCitations = sorted(citations, reverse=True)
    for index in range(len(sortCitations)):
        if (index + 1) >= sortCitations[index]:
            return index + 1
    return len(sortCitations)
#citations = [3, 0, 6, 1, 5]
#citations = [10000, 9999, 9998, 9997, 9996]
citations = [10,10,10,10]
answer = solution(citations)
print(answer)
