from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        s = min(strs,key=len)
        result = ""

        for i in range(len(s)):
            count = 0
            for j in range(strs):
                if s[i] == j[i]:
                    count += 1
            if count == size:
                result += s[i]
            else:
                break
        return result