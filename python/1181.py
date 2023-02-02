from collections import defaultdict
import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

lenWords = defaultdict(set)
for word in words:
    lenWords[len(word)].add(word)

for len in range(1,5001):
    if len in lenWords:
        for word in sorted(lenWords[len]):
            print(word)