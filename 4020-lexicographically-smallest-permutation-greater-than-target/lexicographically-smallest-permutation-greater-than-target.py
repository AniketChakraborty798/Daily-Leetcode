class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        # Step 1: greedily match target as a prefix for as long as possible
        prefix = []
        i = 0
        while i < n:
            idx = ord(target[i]) - 97
            if count[idx] > 0:
                count[idx] -= 1
                prefix.append(target[i])
                i += 1
            else:
                break
        L = i  # length of the exact-matched prefix

        # Step 2: try breaking away at position pos = L, L-1, ..., 0
        pos = L
        while pos >= 0:
            if pos < n:
                t_idx = ord(target[pos]) - 97
                # smallest available char strictly greater than target[pos]
                for c in range(t_idx + 1, 26):
                    if count[c] > 0:
                        count[c] -= 1
                        # fill the rest ascending for the smallest possible suffix
                        suffix_parts = []
                        for cc in range(26):
                            if count[cc] > 0:
                                suffix_parts.append(chr(cc + 97) * count[cc])
                        return "".join(prefix[:pos]) + chr(c + 97) + "".join(suffix_parts)
            if pos > 0:
                # give back prefix[pos-1] so we can test an earlier breakpoint
                count[ord(prefix[pos - 1]) - 97] += 1
            pos -= 1

        return ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.lexGreaterPermutation("abc", "bba"))   # "bca"
    print(sol.lexGreaterPermutation("leet", "code")) # "eelt"
    print(sol.lexGreaterPermutation("baba", "bbaa")) # ""