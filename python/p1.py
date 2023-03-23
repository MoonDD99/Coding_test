def longestChain(words):
    # Write your code here
    result = 1
    for word in words:
        if len(word) == 1:
            continue
        count = 1
        for index in range(len(word)):
            print(word[0:index] + word[index+1:])
            if (word[0:index] + word[index+1:]) in words:
                count += 1
            else:
                result = max(result, count)
                break
    return result

arr = ["bdca"]
longestChain(arr)
