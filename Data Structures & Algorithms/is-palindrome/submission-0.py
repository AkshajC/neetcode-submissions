class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_lowercase, ascii_uppercase
        allowed = ascii_lowercase + ascii_uppercase + "".join([str(i) for i in range(10)])
        s = "".join([ch.lower() for ch in s if ch in allowed])
        print(s)
        return s == s[::-1]