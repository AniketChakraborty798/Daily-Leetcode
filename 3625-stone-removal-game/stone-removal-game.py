class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice = True
        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice = not alice
        # alice is now the player who cannot move, so she loses
        return not alice