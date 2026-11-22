from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=defaultdict(int)
        td=defaultdict(int)

        for i in s :
            sd[i]+=1
        for i in t:
            td[i]+=1
        if sd==td:
            return True
        else:
            return False
        