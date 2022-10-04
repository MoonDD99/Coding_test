def solution(enroll, referral, seller, amount):
    answer = []
    profitMap = {}
    for member in enroll:
        profitMap[member] = 0

    for index in range(0,len(seller)) :
        profitMap[seller[index]] += amount[index] * 100

    for index in range(len(enroll)-1, -1, -1):
        share = int(profitMap[enroll[index]] / 10)

        if referral[index] in profitMap:
            profitMap[enroll[index]] -= share  
            profitMap[referral[index]] += share
        else:
            profitMap[enroll[index]] -= share  
        print("")
        print("-------------------------")
        print("share : " + str(share))
        print("sharing Member : " + enroll[index] + " profitMap : " + str(profitMap[enroll[index]]))
        if referral[index] in profitMap:
            print("shared : " + referral[index] + " profitMap : " + str(profitMap[referral[index]]))
        else :
            print("shared : " + referral[index] + " profitMap : " + " - ")
    for member in enroll: 
        answer.append(profitMap[member])
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

result = solution(enroll, referral, seller, amount)
print(result)