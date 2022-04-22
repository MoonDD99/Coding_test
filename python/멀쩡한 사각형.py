def solution(w,h):
    com_factor = 1 #최대공약수

    #최대공약수 구하기
    for div in range(min(w,h),1,-1):
        if(w%div) == 0 and (h%div) == 0:
            com_factor = div
            break
        
    if com_factor == 1:
    #최대공약수가 1일때
        return w * h - (w + h - 1)
    else :
    #최대공약수가 1이 아닐때
        return w * h - (w + h - com_factor)
    