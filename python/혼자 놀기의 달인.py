from collections import defaultdict
def solution(cards):
    answer = 0
    
    groups = defaultdict(set)
    cards = [-1] + cards
    visited = [False for _ in range(len(cards))]
        
    fMax = 0
    sMax = 0
    
    for index in range(1, len(cards)):
        pCard = cards[index]
        cCard = cards[pCard]
        if not visited[pCard]:
            visited[pCard] = True
            groups[pCard].add(pCard)
            while not visited[cCard]:
                visited[cCard] = True
                groups[pCard].add(cCard)
                cCard = cards[cCard]

    
    for key, value in groups.items():
        print(value)
        if len(value) > fMax:
            sMax = fMax
            fMax = len(value)
        elif len(value) > sMax:
            sMax = len(value)

    return fMax * sMax