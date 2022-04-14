#Fail Test : 14
#Score : 93.3 / 100.0

def solution(lottos, win_nums):
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