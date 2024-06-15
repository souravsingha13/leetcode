class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in lookup: # The character is a closing bracket
# Pop the top element from the stack if it's not empty; otherwise assign a dummy value
                top_element=stack.pop() if stack else '#'
                if lookup[char] != top_element:
                    return False
            else: # The character is an opening bracket
                stack.append(char)
        return not stack