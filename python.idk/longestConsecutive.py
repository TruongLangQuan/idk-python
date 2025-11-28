from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        streak = 0
        i = 0

        if len(nums) <= 1:
            return len(nums)
        
        curr,res = nums[0],0
        
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
        
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res,streak)
        return res