class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize - 1
        sum_array = max_sum
        for i in nums:
            if sum_array < 0:
                sum_array = i
            else:
                sum_array += i
            max_sum = max(max_sum, sum_array)
        
        return max_sum

        