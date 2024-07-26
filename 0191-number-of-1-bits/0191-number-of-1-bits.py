class Solution:
    def __init__(self):
        self.count = 0
    def hammingWeight(self, n: int) -> int:
        if n == 1:
            self.count += 1
            return self.count
        if n == 0:
            return self.count
        remainder = n%2
        if remainder == 1:
            self.count = self.count +1 
        n = round(n // 2)
        return self.hammingWeight(n)
 