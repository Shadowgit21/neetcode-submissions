class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        frequencyy = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in frequency:
                frequency[ch] +=1
            else:
                frequency[ch]=1
        for ch in t:
            if ch in frequencyy:
                frequencyy[ch] +=1
            else:
                frequencyy[ch]= 1
        
        return frequency == frequencyy

