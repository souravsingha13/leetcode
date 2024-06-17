class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums and max(nums)<target:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
                elif nums[i]==target:
                    return i
                else:
                    pass
            