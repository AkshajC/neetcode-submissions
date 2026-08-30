class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from string import ascii_lowercase

        alphabet_s = dict(zip(ascii_lowercase, [0]*26))
        alphabet_t = dict(zip(ascii_lowercase, [0]*26))

        for letter in s:
            alphabet_s[letter]+=1
        for letter in t:
            alphabet_t[letter]+=1
        return alphabet_s == alphabet_t