class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix_val={0:1}
        s=0
        ans=0

        for i in nums:
            s+=i
            ques=s%k
            if ques in prefix_val:
                ans+=prefix_val[ques]
            prefix_val[ques]=prefix_val.get(ques,0)+1
        return ans
