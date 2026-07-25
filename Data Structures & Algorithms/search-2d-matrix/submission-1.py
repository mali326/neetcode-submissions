class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m2 = [x for xs in matrix for x in xs]
        l,r=0,len(m2)-1
        while l <= r:
            mid = (l+r)//2
            if m2[mid] == target:
                return True
            if m2[mid]<target:
                l = mid+1
            else:
                r=mid-1
        return False
