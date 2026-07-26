class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]: # l sorted
                if nums[l]<=target<=nums[mid]: # target in range
                    r = mid-1
                else:
                    l=mid+1
            else: #nums[mid]<=nums[r]: #r sorted
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1