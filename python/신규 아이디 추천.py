import re

def solution(new_id):
    #score = 100.0 / 100.0
    
    answer = ''
    
    #Level 1
    new_id = new_id.lower()
    
    #Level 2
    new_id = re.sub('[^a-z0-9-_.]','',new_id)
    
    #Level 3
    new_id = re.sub('\.\.+',".",new_id)

    #Level 4
    new_id = new_id.strip(".")

    #Level 5
    if new_id == "":
        new_id = "a"

    #Level 6
    new_id = new_id[0:15]
    new_id = new_id.rstrip(".")

    #Level 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[len(new_id)-1]

    answer = new_id
    return answer

answer = "abcdefghijklmn.p"
print(solution(answer))