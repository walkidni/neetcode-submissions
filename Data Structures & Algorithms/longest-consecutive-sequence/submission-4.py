class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seq_start = []
        seq_lens = defaultdict(int)
        for n in num_set :
            if n-1 not in num_set:
                seq_start.append(n)
        for n in seq_start:
            m = n
            while m in num_set:
                seq_lens[n]+=1
                m+=1
        return max(seq_lens.values()) if len(seq_lens) else 0