class Solution(object):
    def firstUniqChar(self, s):
        d = {}

        # Count characters
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        # Find first character with count 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1