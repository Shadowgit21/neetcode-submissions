class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        frequency2 = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] +=1
            else:
                frequency[ch] = 1
        for ch in t:
            if ch in frequency2:
                frequency2[ch] +=1
            else:
                frequency2[ch] = 1
        return frequency == frequency2
        