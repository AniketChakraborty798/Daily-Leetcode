class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first, last = {}, {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        candidates = []
        for c in first:
            start, end = first[c], last[c]
            j = start
            valid = True
            while j <= end:
                ch = s[j]
                if first[ch] < start:
                    valid = False
                    break
                end = max(end, last[ch])
                j += 1
            if valid:
                candidates.append((end, start))

        candidates.sort()

        res = []
        last_end = -1
        for end, start in candidates:
            if start > last_end:
                res.append(s[start:end + 1])
                last_end = end
        return res