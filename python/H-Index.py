def solution(citations):
    citations.sort()
    lenCitations = len(citations)
    print(citations)
    for h in range(lenCitations-1,0,-1):
        if lenCitations-(h-1) >= h and citations[h+1] >= citations[h]:
            return h


citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(answer)