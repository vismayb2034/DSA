class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum={0:1}
        s=0
        count=0

        for i in nums:
            s+=i
            q=s-k
            
            count+=prefix_sum.get(q,0)
            prefix_sum[s] = prefix_sum.get(s,0) + 1
        return count

