class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in loc:
                return [loc[comp], i]
            else:
                loc[num] = i