def solution(scores):
    answer = 1

    WHAttitude = scores[0][0]
    WHEvaluation = scores[0][1]
    WHScore = WHAttitude + WHEvaluation
    
    threshold = 0
    scores.sort(key=lambda x: (-x[0],x[1]))
    
    for attitude, evaluation in scores:
        if attitude > WHAttitude and evaluation > WHEvaluation:
            return -1
        if threshold <= evaluation:
            if (attitude+evaluation) > WHScore:
                answer +=1
            threshold = evaluation
    return answer