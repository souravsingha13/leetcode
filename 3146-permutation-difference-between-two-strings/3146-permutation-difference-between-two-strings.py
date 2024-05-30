class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        absolute_diff = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    absolute_diff = absolute_diff+ abs(i-j)
        return absolute_diff