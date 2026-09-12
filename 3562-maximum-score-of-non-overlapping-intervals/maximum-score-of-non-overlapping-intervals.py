from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])  # sort by right endpoint
        Ls = [intervals[i][0] for i in order]
        Rs = [intervals[i][1] for i in order]
        Ws = [intervals[i][2] for i in order]

        NEG = float('-inf')
        # dp[i][k] = (score, sorted tuple of original indices) using exactly k
        # intervals chosen among the first i (r-sorted) intervals
        dp = [[(NEG, None) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, ())

        def insert_sorted(tup, val):
            lst = list(tup)
            pos = bisect.bisect_left(lst, val)
            lst.insert(pos, val)
            return tuple(lst)

        for i in range(1, n + 1):
            pos = i - 1
            orig = order[pos]
            l, w = Ls[pos], Ws[pos]
            # count of earlier intervals (in r-sorted order) with r < l
            p = bisect.bisect_left(Rs, l, 0, pos)

            for k in range(5):
                best = dp[i - 1][k]                 # option: skip current interval
                if k >= 1:
                    prev_score, prev_tuple = dp[p][k - 1]
                    if prev_score != NEG:            # option: take current interval
                        cand_score = prev_score + w
                        cand_tuple = insert_sorted(prev_tuple, orig)
                        if (cand_score > best[0] or
                                (cand_score == best[0] and cand_tuple < best[1])):
                            best = (cand_score, cand_tuple)
                dp[i][k] = best

        best_ans = (NEG, None)
        for k in range(5):
            score, tup = dp[n][k]
            if score == NEG:
                continue
            if (score > best_ans[0] or
                    (score == best_ans[0] and (best_ans[1] is None or tup < best_ans[1]))):
                best_ans = (score, tup)

        return list(best_ans[1]) if best_ans[1] is not None else []