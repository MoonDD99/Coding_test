import math

def solution(enroll, referral, seller, amount):

    enrollDict = dict(zip(enroll, referral)) #{판매원 : 추천인}
    profitDict = dict(zip(enroll, [0 for i in range(len(enroll))])) #{판매원 : 정산금}

    
    for index in range(len(seller)):
        share = amount[index] * 100 # 이익
        target = seller[index] # 추천인

        while True :
            if share < 10 : # 추천인에게 돌아가는 이익이 10보다 작은경우
                profitDict[target] += share
                break 
            else : 
                profitDict[target] += math.ceil(share * 0.9) # 이익의 90%
                if enrollDict[target] == "-": #추천인이 민호인 경우
                    break
                share = math.floor(share*0.1) #이익의 10%
                target = enrollDict[target] #현재 target의 추천인
                    
    return list(profitDict.values())

import math
def solution(enroll, referral, seller, amount):
    answer = []
    childParent = {}
    childProfit = {}
    
    for index in range(len(enroll)):
        child = enroll[index]
        parent = referral[index]
        
        childParent[child] = parent
        childProfit[child] = 0
    
    for index in range(len(seller)):
        child = seller[index]
        profit = amount[index] * 100 

        while True:
            if profit < 10:
                childProfit[child] += profit
                break
            else:
                childProfit[child] += math.ceil(profit*0.9)
                child = childParent[child] 
                if child == "-":
                    break
                profit = math.floor(profit*0.1)
                      
    
    for index in range(len(enroll)):
        answer.append(childProfit[enroll[index]])
        
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

result = solution(enroll, referral, seller, amount)
print(result)