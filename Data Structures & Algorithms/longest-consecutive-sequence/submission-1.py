class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 1:
            return len(nums) 
        nums.sort()
        lenmax = 1
        ans = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                lenmax += 1
            else:
                ans = max(lenmax,ans)
                lenmax = 1
        return max(ans,lenmax)           


