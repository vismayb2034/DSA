import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):

        l = []

        for i in range(len(profits)):
            l.append([capital[i], profits[i]])

        l.sort()

        i = 0
        heap = []

        while k:

            # Add every project we can currently afford
            while i < len(l) and l[i][0] <= w:
                heapq.heappush(heap, -l[i][1])
                i += 1

            # No project is affordable
            if not heap:
                break

            # Take the project with maximum profit
            w += -heapq.heappop(heap)

            k -= 1

        return w

        