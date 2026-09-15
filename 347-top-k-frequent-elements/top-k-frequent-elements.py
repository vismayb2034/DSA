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

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        heap = []

        for num in freq:
            p = Pair(freq[num], num)

            heapq.heappush(heap, p)

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            p = heapq.heappop(heap)
            ans.append(p.second)

        return ans