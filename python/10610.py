n = input()

if '0' not in n:
    print("-1")
else : 
    sum = 0
    for num in n:
        sum += int(num)
    if sum % 3 != 0:
        print("-1")
    else:
        sortN = sorted(n, key=lambda x:int(x), reverse=True)
        print(''.join(sortN))
