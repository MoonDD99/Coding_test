import math

def solution(enroll, referral, seller, amount):

    enrollDict = dict(zip(enroll, referral))
    profitDict = dict(zip(enroll, [0 for i in range(len(enroll))]))

    
    for index in range(len(seller)):
        share = amount[index] * 100
        target = seller[index]

        while True :
            if share < 10 : 
                profitDict[target] += share
                break
            else : 
                profitDict[target] += math.ceil(share * 0.9)
                if enrollDict[target] == "-": 
                    break
                share = math.floor(share*0.1)
                target = enrollDict[target]
                    
    return list(profitDict.values())

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

result = solution(enroll, referral, seller, amount)
print(result)