class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen :
                print(s[l:r])
                found_at = seen[s[r]]
                for c in s[l:found_at+1]:
                    seen.pop(c,0) 
                l = found_at + 1
                seen[s[r]] = r
                continue
            current_len = r - l + 1
            longest = max(longest, current_len)
            seen[s[r]] = r
        return longest

        