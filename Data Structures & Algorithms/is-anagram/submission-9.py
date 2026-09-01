class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        frequency1 = {}
        frequency2 = {}
        for num in s:
            if num in frequency1:
                frequency1[num] +=1
            else:
                frequency1[num] = 1
        for num in t:
            if num in frequency2:
                frequency2[num] +=1
            else:
                frequency2[num] = 1
        return frequency1 == frequency2
        
    
        