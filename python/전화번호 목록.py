def solution(phone_book):
    phoneBookDict = {}

    for phoneNumber in phone_book:
        phoneBookDict[phoneNumber] = 0

    for phoneNumber in phone_book:
        for index in range(len(phoneNumber)):
            if phoneBookDict.get(phoneNumber[:index]) != None:
                #print(phoneNumber[:index])
                return False
    
    return True

#phone_book = ["119", "97674223", "1195524421"]
#phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
answer = solution(phone_book)
print(answer)