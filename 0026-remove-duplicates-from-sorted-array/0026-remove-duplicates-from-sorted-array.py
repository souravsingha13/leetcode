class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 1
        for index in range(1,len(nums)):
            if nums[index]!=nums[index-1]:
                nums[flag] = nums[index]
                flag += 1
        return flag