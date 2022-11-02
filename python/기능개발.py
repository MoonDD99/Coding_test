from collections import deque
def solution(progresses, speeds):
    answer = []
    
    proQue = deque(progresses)
    speedsQue = deque(speeds)
    


    #proQue가 empty가 아닐때까지  
    while proQue:
        print(proQue)
        #proQue = proQue에서 왼쪽 pop
        progress = proQue.popleft()
        #speed = speedsQue 왼쪽 pop
        speed = speedsQue.popleft()
        #count 0으로 초기화
        count = 0
        #값이 100보다 작으면
        if progress < 100:
            #proQue에 있는 모든 원소들 += speed
            proQue.appendleft(progress)
            speedsQue.appendleft(speed)
            for i in range(len(proQue)):
                proQue[i] += speedsQue[i]
        #값이 100보다 크면
        else:
            #proQue가 100보다 클때까지
            if len(proQue) >= 1:
                while progress >= 100 and proQue:
                    #count += 1
                    count += 1
                    #proQue = proQue에서 왼쪽 pop
                    progress = proQue.popleft()
                    #speed = speedsQue 왼쪽 pop
                    speed = speedsQue.popleft()
                proQue.appendleft(progress)
                speedsQue.appendleft(speed)
            else:
                count += 1
        #count가 0이 아니면
        if count != 0:
            answer.append(count)
            #answer에 count 추가
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

answer = solution(progresses,speeds)
print(answer)