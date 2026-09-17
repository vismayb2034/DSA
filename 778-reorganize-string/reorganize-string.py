class Pair:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __lt__(self,other):
        if self.first != other.first:
            return self.first > other.first
        return self.second > other.second

class Solution(object):
    def reorganizeString(self, s):
        d = {}
        heap =[]
        for i in s:
            d[i] = d.get(i,0) + 1
        
        for ele,freq in list(d.items()):
            heapq.heappush(heap,Pair(freq,ele))
        
        seat = 0
        ans =""
        while heap:
            p = heapq.heappop(heap)
            if seat==0 or ans[seat-1] != p.second:
                ans += p.second
                p.first -= 1
                seat += 1
                if p.first > 0:
                    heapq.heappush(heap,p)
            
            else:
                if not heap:
                    return ""
                p1 = heapq.heappop(heap)
                ans += p1.second
                p1.first -= 1
                seat += 1
                if p1.first > 0:
                    heapq.heappush(heap,p1)
                heapq.heappush(heap,p)
        return ans
