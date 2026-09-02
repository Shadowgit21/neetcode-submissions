class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] =1
        result = []
        for _ in range(k):
            max_num = None
            max_count = 0
            for num in frequency:
                if frequency[num] > max_count:
                    max_count = frequency[num]
                    max_num = num
            result.append(max_num)
            del frequency[max_num]
        return result
            
        