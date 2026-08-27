class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        a = []

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [1, i]
                a.append(i)
            else:
                d[s[i]][0] += 1

                if d[s[i]][0] == 2:
                    a.remove(d[s[i]][1])

        if a:
            return a[0]

        return -1