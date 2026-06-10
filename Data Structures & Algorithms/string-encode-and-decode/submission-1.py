class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs :
            l = len(s)
            encoded += f'#{l}#{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            assert(s[i] == "#")
            j = i+1
            l = '' 
            while s[j] != "#":
                l+=s[j]
                j+=1
            l = int(l)
            strs.append(s[j+1:j+l+1])
            i = j+l+1
        return strs