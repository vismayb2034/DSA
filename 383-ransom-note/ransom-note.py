class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = {}

        for ch in magazine:
            d[ch] = d.get(ch, 0) + 1

        for ch in ransomNote:
            if d.get(ch, 0) == 0:
                return False
            d[ch] -= 1

        return True