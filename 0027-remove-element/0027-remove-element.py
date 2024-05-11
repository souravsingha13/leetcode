class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i,num in enumerate(nums):
            if num != val:
                nums[index] = nums[i]
                index += 1
        return index