class Solution(object):
    def sortedSquares(self, nums):
        pos = []
        neg = []
        res = []

        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        if len(neg) == 0:
            res = [x*x for x in pos]
            return res

        if len(pos) == 0:
            neg = [x*x for x in neg]
            neg.reverse()
            return neg

        j, k = 0, 0

        neg = [x*x for x in neg]
        pos = [x*x for x in pos]
        neg.reverse()

        while j < len(pos) and k < len(neg):
            if pos[j] < neg[k]:
                res.append(pos[j])
                j += 1
                continue
            else:
                res.append(neg[k])
                k += 1
                continue

        while j < len(pos):
            res.append(pos[j])
            j += 1

        while k < len(neg):
            res.append(neg[k])
            k += 1

        return res

        