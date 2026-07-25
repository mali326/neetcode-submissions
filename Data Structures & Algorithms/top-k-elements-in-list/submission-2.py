from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter to get freq of each number use most_common(k)
        ct = Counter(nums).most_common(k)
        return [x[0] for x in ct]
        