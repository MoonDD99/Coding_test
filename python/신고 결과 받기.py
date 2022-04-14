
from xml.dom.minidom import Identified


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    #Score : 100.0 / 100.0

    answer = []
    num_email = dict() #id : 이메일 받을 갯수
    num_decl = dict() #id : 신고받은 횟수
    toEmail = dict() #id : {나를 신고한 id들}
    for id in id_list:
        num_email[id] = 0
        num_decl[id] = 0
        st = set()
        toEmail[id] = st
    
    #report에서 나를 신고한 id들 정리해서 toEmail에 저장
    for dec in report :
        result = dec.split(" ")
        toEmail[result[1]].add(result[0])
    #toEmail에 value의 len = 신고받은 횟수
    for id in toEmail:
        num_decl[id] = len(toEmail[id])
    #num_decl에서 value가 k보다 크면
    for key in num_decl:
        if k <= num_decl[key]:
    #toEmail[key]의 value를 순차탐색해서 num_email을 1씩 키워줌
            id_set = toEmail[key]
            for id in id_set:
                num_email[id] += 1
    #id_list의 값들은 num_email에서 찾아서 result에 값들을 넣어줌
    """
    print(num_email)
    print(num_decl)
    print(toEmail)"""
    for id in id_list:
        answer.append(num_email[id])
    
    return answer

def solution1(id_list, report, k):
    answer = [0] * len(id_list)
    decl_result = {x : 0 for x in id_list}

    for decl in set(report):
        decl_result[(decl.split())[1]] += 1

    for decl in set(report):
        if decl_result[(decl.split())[1]] >= k:
            answer[id_list.index(decl.split()[0])] += 1
    
    return answer

answer = solution1(id_list,report,k)
print(answer)