class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        alen = len(a)-1
        blen = len(b)-1
        carry = 0
        while alen>=0 or blen>=0 or carry:
            carry += int(a[alen]) if alen>=0 else 0
            carry += int(b[blen]) if blen>=0 else 0
            result = str(carry%2)+result
            carry = carry//2
            alen -= 1
            blen -= 1
        return result