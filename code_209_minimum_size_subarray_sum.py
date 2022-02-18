import math
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # base cases to exit quickly
        if not nums:
            return 0
        if target in nums:
            return 1
        
        n = len(nums)
        current_sum = 0
        pointer_left = 0
        min_count = math.inf
        for pointer_right in range(n):
            current_sum += nums[pointer_right]
            
            while current_sum >= target and pointer_left <= pointer_right:
                min_count = min(min_count, pointer_right-pointer_left + 1)
                current_sum -= nums[pointer_left]
                pointer_left += 1       
        
        min_count = 0 if min_count == math.inf else min_count
        return min_count