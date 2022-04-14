

def solution(lottos, win_nums):
    #Fail Test : 14
    #Score : 93.3 / 100.0
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    
    win = lottos_set & win_nums_set
    count = 0
    for lotto in lottos:
        if lotto == 0:
            count += 1
    
    answer = []
    if len(win) >= 2:
        min = 7-len(win)
    else :
        min = 6
        
    max = 7-(len(win)+count)
    answer.append(max)
    answer.append(min)
    return answer

def solution1(lottos, win_nums):
    #Score : 100.0 / 100.0
    rank = [6,6,5,4,3,2,1]
    zero = lottos.count(0)

    win = 0
    for num in win_nums:
        if num in lottos:
            win += 1
    max = rank[win+zero]
    min = rank[win]
    answer = [max,min]
    return answer