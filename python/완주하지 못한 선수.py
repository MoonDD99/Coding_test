def solution(participant, completion):
    participantMap = {}
    hashSum = 0 

    for part in participant:
        participantMap[hash(part)] = part
        hashSum += hash(part)

    for element in completion:
        hashSum -= hash(element)
    
    return participantMap[hashSum]
        
#participant = ["leo", "kiki", "eden"]
#completion = ["eden", "kiki"]

#participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
#completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = solution(participant,completion)
print(answer)

