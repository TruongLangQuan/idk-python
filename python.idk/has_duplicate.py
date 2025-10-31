from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortnums = nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                return False
        return True