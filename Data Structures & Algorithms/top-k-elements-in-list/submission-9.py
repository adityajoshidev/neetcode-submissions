class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        bucket=[[] for i in range(len(nums)+1)]
        for n in nums:
            counts[n]=counts.get(n,0)+1
        for n,c in counts.items():
            bucket[c].append(n)
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)
                if len(result)==k:
                    return result