import heapq

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        return self.second < other.second


class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1

        heap = []

        for ele, freq in list(d.items())[:k]:
            heapq.heappush(heap, Pair(freq, ele))

        for ele, freq in list(d.items())[k:]:
            if heap[0].first < freq:
                heapq.heappush(heap, Pair(freq, ele))
                heapq.heappop(heap)

        ans = []

        while heap:
            p = heapq.heappop(heap)
            ans.append(p.second)

        return ans