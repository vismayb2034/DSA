class Solution(object):
    def findMaxLength(self, nums):
        zero=0
        one=0
        prefix_val={}
        ans=0

        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            ques=zero-one

            if ques == 0:
                ans= max(ans,i+1)

            if ques in prefix_val:
                l=i-prefix_val[ques]
                ans=max(ans,l)
                
            else:
                prefix_val[ques] = i
        return ans