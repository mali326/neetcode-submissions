import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        res = math.prod(nums)
        for x in nums:
            if x != 0:
                ans.append(res//x)
            else:
                nums2 = nums[:]
                nums2.remove(0)
                ans.append(math.prod(nums2))
        return ans
            