class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) <= 1):
            return len(s)
        l = 0
        r = 1
        cur_set = set([s[l]])
        max_len = 1

        while(r < len(s)):
            # print(f"{l}: {s[l]}, {r}: {s[r]}")

            if s[r] in cur_set:
                while(s[l] != s[r]):
                    cur_set.discard(s[l])
                    l += 1

                # cur_set.add(s[l])
                l += 1
                
            else:
                # print(f"adding {s[r]}")
                cur_set.add(s[r])
                # print(cur_set)
                max_len = max(max_len, len(cur_set))
                # print(len(cur_set))
            r += 1
            # print(cur_set)
        return max_len
            