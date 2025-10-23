from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count, resultarr = 0,[]
        sortnum = sorted(nums)

        for i in range(sortnum):
            pass