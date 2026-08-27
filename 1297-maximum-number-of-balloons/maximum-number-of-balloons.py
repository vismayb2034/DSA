class Solution(object):
    def maxNumberOfBalloons(self, text):
        s = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        d = {}
        mini = float('inf')

        for ch in text:
            d[ch] = d.get(ch, 0) + 1

        for ch in s:
            if d.get(ch, 0) < s[ch]:
                return 0

            cur = d[ch] // s[ch]
            mini = min(cur, mini)

        return mini