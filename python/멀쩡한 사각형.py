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
    
def solution1(w,h):
    gcd = 1
    for i in range(min(w,h),0,-1):
        if ((w%i) == 0) and ((h%i) == 0):
            gcd = i
            break
    return w*h - (w + h - gcd)

def gcd(a,b):
    if a == 0:
        return b
    else:
        gcd(b%a, a)