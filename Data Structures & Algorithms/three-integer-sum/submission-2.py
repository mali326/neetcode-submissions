class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        ans = []
        nums.sort()
        # -nums[i]=nums[j]+nums[k]
        for i in range(len(nums)-1):
            target = -1*nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==target:
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else: #nums[j]+nums[k]>target
                    k-=1
        return ans
                
