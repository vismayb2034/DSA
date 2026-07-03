class Solution(object):
    def subarraySum(self, nums, k):
        prefix_counts = {0: 1}
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            needed = running_sum - k
            if needed in prefix_counts:
                count += prefix_counts[needed]
            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1
        
        return count 