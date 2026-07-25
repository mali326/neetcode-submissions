import math
# calc prod for each num with list.pop(i)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            temp = nums[:i]+nums[i+1:]
            output.append(math.prod(temp))
        return output