class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def most_common_count(counter: dict) -> int:
            res = 0
            for v in counter.values():
                res = max(res, v)
            return res
        res = 0
        count = defaultdict(int)
        r, l, window_size = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] += 1
            v = most_common_count(count)
            replaceable = r - l + 1 - v
            window_size += 1
            if replaceable > k:
                count[s[l]] -= 1 
                l+=1
                window_size -= 1
            res = max(window_size, res)
        return res
            
            


