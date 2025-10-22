class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        
        for dupe in nums:
            if nums.count(dupe) > 1:
                return True
        return False