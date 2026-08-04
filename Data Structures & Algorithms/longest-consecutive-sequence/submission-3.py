class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_subsequence = 1
        current_sequence = 1
        if len(nums)==0:
                return 0
        nums.sort()
        for i in range (1,len(nums)):

            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                current_sequence +=1
            else:
                current_sequence =1
            if current_sequence> longest_subsequence:
                longest_subsequence = current_sequence
            
        return longest_subsequence
