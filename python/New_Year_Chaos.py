def minimumBribes(q):
    # Write your code here
    result = 0
    minElements = (sys.maxsize, sys.maxsize)
    for index,element in reversed(list(enumerate(q,1))):
        if (element - index) > 2:
            print("Too chaotic")
            return
        if element > minElements[1]:
            result += 2
        elif element > minElements[0]:
            result += 1
        
        if element < minElements[0]:
            minElements = (element, minElements[0])
        elif element < minElements[1]:
            minElements = (minElements[0], element)
    print(result)