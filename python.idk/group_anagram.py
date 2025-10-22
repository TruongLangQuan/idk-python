from email.policy import default
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = default(list)
        for ch in strs:
            sortch = "".join(sorted(ch))
            res[sortch].append(ch)
        return list(res.value())