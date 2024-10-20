
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        start = 0
        end = 0 
        count = 0
        product = 1
        for end in range(len(nums)):
            product *= nums[end]
            
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
                
            count += (end - start + 1)
        return count