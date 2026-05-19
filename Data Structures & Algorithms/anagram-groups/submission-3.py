class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i, s in enumerate(strs):
            key = frozenset(Counter(s).items())
            hmap[key].append(i)
        res = []
        for key, indices in hmap.items():
            res.append([strs[i] for i in indices])
        return res