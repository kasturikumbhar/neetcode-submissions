from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for i in range(len(strs)):
            s=''.join(sorted(strs[i]))
            seen[s].append(strs[i])
        output=[]
        for k,v in seen.items():
            output.append(v)

        return output



        