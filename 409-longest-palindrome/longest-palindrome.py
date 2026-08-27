class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        i = 0

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in d:
            i += (d[ch] // 2) * 2

        for ch in d:
            if d[ch] % 2 == 1:
                i += 1
                break

        return i