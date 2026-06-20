from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = sorted(tuple(Counter(nums).items()), key= lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(counts[i][0])
        return output