class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        result = []
        for i in range(len(digits)):
            num = num + str(digits[i])
        num = int(num)+1
        num = str(num)
        for i in range(len(num)):
            result.append(int(num[i]))
        return result