import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums).most_common(k)
        return [x[0] for x in ct]

