class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)
        return list(d.values())