from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) +1

        arr = []
        for number,cnt in count.items():
            arr.append([cnt,number])
            arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
     
nums = [7,7]
k = 1

idk = Solution()

print(idk.topKFrequent(nums,k))