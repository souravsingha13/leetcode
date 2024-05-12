class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        l = len(words)
        return len(words[l-1])