class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            l = str(len(s))
            ans += l.zfill(4)
            ans += s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        totLen = len(s)
        strs = []
        while i<totLen:
            lenS=s[i:i+4]
            l = int(lenS)
            i+=4
            strs.append(s[i:i+l])
            i+=l
        return strs
