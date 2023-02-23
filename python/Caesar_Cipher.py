def caesarCipher(s, k):
    # 대문자 : 65 ~ 90 소문자 : 97 ~ 122
    # 대문자 rotate : 91 <= index + k <= 90 + k
    # 소문자 rotate : 123 <= index + k <= 122 + k
    # 변환 index + k - 26
    
    result=""
    k = k % 26
    for char in s:
        ordChar = ord(char)
        if (65 <= ordChar <= 90) or (97<= ordChar <= 122):
            ordChar = ordChar + k    
            if (91 <= ordChar <= (90 + k)) or (123 <= ordChar <= (122 + k)):
                ordChar = ordChar - 26
        result += chr(ordChar)
    return result
    
s = "middle-Outz"
k = 2
answer = caesarCipher(s,k)
print(answer)
