from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)):
            if arr[i] != 0:
                i += 1
            else:
                arr.append(0)