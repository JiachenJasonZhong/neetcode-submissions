class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int)
        for num in nums:
            numdict[num]+=1

        sortednums = sorted(
            numdict,
            key = lambda x: numdict[x],
            reverse = True
            )
        return sortednums[:k]
