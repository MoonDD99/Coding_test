def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    newHour = hour % 12
    if s[8:10] =='PM':
        newHour = (hour % 12) + 12
        return str(newHour) + s[2:8]
    else:
        return '0' + str(newHour) + s[2:8]

s = "04:59:59AM"
answer = timeConversion(s)
print(answer)