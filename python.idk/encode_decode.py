from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, res = [],""

        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size,res,i = [],[],0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            size.append(int(curr))
            i += 1
        i += 1
        for sz in size:
            res.append(s[i:i + sz])
            i += sz
        return res
    
string = ["neet","code","love","you"]

solution = Solution()

result = solution.encode(string)
result2 = solution.decode(result)

print(result)
print(result2)