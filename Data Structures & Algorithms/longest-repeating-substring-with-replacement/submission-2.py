class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        l = 0
        count = collections.defaultdict(int)
        max_f = 0
        maxLen = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            
        return maxLen
            