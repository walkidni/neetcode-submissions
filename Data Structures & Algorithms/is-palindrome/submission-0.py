class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(c.lower() for c in s if c.isalnum())
        return ss == ss[::-1]
        