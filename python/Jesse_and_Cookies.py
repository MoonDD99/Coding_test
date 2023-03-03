import heapq
def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    count = 0 
    
    while len(A) >= 2:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        
        if first >= k:
            return count
        count += 1
        
        heapq.heappush(A,(first + 2 * second))
    
    if heapq.heappop(A) >= k:
        return count
    return -1 