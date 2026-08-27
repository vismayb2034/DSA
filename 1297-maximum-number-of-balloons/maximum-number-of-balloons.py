class Solution(object):
    def maxNumberOfBalloons(self, text):
        s = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        d = {}

        for ch in text:
            d[ch] = d.get(ch, 0) + 1

        i = 0

        while True:
            for ch in s:
                if d.get(ch, 0) - s[ch] < 0:
                    return i
                d[ch] -= s[ch]

            i += 1