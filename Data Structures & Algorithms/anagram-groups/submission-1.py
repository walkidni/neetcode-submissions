class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        sorted_strs = list(map(lambda x: "".join(sorted(x)), strs))
        
        for i, s in enumerate(sorted_strs):
            if s not in hmap:
                hmap[s] = [] 
            hmap[s].append(i)
        res = []
        for ss, indices in hmap.items():
            group = [strs[i] for i in indices]
            res.append(group)
        return res
