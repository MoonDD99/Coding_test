
from turtle import right


def solution(numbers, hand): 
    answer = ''
    lr = hand[0].upper()
    number_location = {1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 7:(3,1), 8:(3,2), 9:(3,3), 0:(4,2)}
    left_location = (4,1)
    right_location = (4,3)
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            left_location = number_location[number]
            print("left_location:", left_location)
        elif number == 3 or number == 6 or number == 9 :
            answer += "R"
            right_location = number_location[number]
            print("right_location:", right_location)
        else :
            len_left = abs(number_location[number][0] - left_location[0]) + abs(number_location[number][1] - left_location[1])
            len_right = abs(number_location[number][0] - right_location[0]) + abs(number_location[number][1] - right_location[1])
            if len_left < len_right:
                forAdd = "L"
                left_location = number_location[number]
            elif len_right < len_left:
                forAdd = "R"
                right_location = number_location[number]
            else: 
                forAdd = lr
                if lr == "L":
                    left_location = number_location[number]
                else :
                    right_location = number_location[number]
            answer += forAdd
            print("left_location:", left_location)

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers,hand)
print(result)