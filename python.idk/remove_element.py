from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idk = nums.count(val)
        for i in range(idk):
            nums.remove(val)