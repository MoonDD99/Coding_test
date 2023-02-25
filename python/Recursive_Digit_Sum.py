def superDigit(n, k):
    # Write your code here
    n = n * k
    print(n[0])
    while int(n) > 9:
        sum = 0 
        for char in n:
            sum += int(char)
        n = str(sum)
    return n
 
n, k = "148",3
answer = superDigit(n,k)