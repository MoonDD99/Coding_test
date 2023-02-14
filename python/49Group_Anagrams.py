from collections import defaultdict
class Solution:
    def groupAnagrams(strs):
        answer = []
        strAnagrams = defaultdict(list)
        for string in strs:
            sortString = ''.join(sorted(string))
            strAnagrams[sortString].append(string)
        
        for value in strAnagrams.values():
            answer.append(value)
        return answer

strs = ["eat","tea","tan","ate","nat","bat"]
output = Solution.groupAnagrams(strs)
print(output)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        strAnagrams = defaultdict(list)
        for string in strs:
            sortString = ''.join(sorted(string))
            strAnagrams[sortString].append(string)
        
        for value in strAnagrams.values():
            answer.append(value)
        return answer