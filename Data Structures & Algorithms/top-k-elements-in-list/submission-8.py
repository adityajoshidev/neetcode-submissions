import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pq=[]
        # i=0
        # nums.sort()
        # while i<len(nums):
        #     num=nums[i]
        #     count=nums.count(num)
        #     heapq.heappush(pq,(-count,num))
        #     i+=count
        # clist=[]
        # for i in range(k):
        #     if pq:
        #         count,num=heapq.heappop(pq)
        #         clist.append(num)
        # return clist
        counts=Counter(nums)
        return [x[0] for x in counts.most_common(k)]