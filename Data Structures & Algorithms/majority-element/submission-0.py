class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        n = len(nums)
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] = 1
            if frequency[num] >= n/2:
                return num

        