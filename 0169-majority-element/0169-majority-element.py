class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dublicate_list = {}
        for num in nums:
            if num not in  dublicate_list:
                dublicate_list[num] = [num]
            else:
                dublicate_list[num].append(num)
        max_key = max(dublicate_list, key=lambda k : len(dublicate_list[k]))
        return max_key