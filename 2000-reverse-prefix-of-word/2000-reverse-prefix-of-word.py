class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                first_sub_str = word[:i+1]
                second_sub_str = word[i+1:]
                rev_first_sub_str = first_sub_str[::-1]
                return rev_first_sub_str+second_sub_str
        return word
                