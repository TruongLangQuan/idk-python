from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = nums.sort()
        streak = 0
        i = 0

        if not nums:
            return 0
        
        curr,res = nums[0],0
        
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0
        
        while i < len(nums) and nums[i] == curr:
            if nums[i] == curr:
                streak += 1
                curr += 1
                res += streak
        return res