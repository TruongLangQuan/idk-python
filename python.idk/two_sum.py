class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i,num in enumerate(nums):
            result = target - num
            if result in num_map:
                return [num_map[result],i]
            num_map[num] = i
        return []

idk = input()
mylist = list(map(int, idk.split()))
target = int(input())

solution = Solution()
result = solution.twoSum(mylist,target)

print(result)