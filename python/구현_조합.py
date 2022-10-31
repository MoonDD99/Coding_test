# arr 배열에서 n개의 조합을 구할때
def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for c in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + c)
    return result

arr = [1,2,3]
print(comb(arr,1))
print(comb(arr,2))
print(comb(arr,3))