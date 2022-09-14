def solution(citations):
    citations.sort()
    lenCitations = len(citations)
    for h in range(lenCitations):
        if citations[h] >= lenCitations - h:
            return lenCitations - h
    return 0


citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(answer)