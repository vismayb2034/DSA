class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        s = sum(nums)
        n = len(nums)
        
        for i in range(n):
            right = s - nums[i] - left
            if(left == right):
                return i
            left += nums[i]
            
        return -1