class Solution(object):
    def longestPalindrome(self, s):
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        i = 0
        odd = False

        for ch in d:
            i += (d[ch] // 2) * 2

            if d[ch] % 2 == 1:
                odd = True

        if odd:
            i += 1

        return i