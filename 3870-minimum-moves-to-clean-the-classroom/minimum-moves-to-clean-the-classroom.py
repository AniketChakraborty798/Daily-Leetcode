from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_positions = []
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter_positions.append((r, c))

        k = len(litter_positions)
        if k == 0:
            return 0

        litter_id = [[-1] * n for _ in range(m)]
        for i, (r, c) in enumerate(litter_positions):
            litter_id[r][c] = i

        full_mask = (1 << k) - 1
        E = energy
        estep = E + 1
        mstep = 1 << k

        def encode(r, c, e, mask):
            return ((r * n + c) * estep + e) * mstep + mask

        visited = bytearray(m * n * estep * mstep)

        sr, sc = start
        start_state = encode(sr, sc, E, 0)
        visited[start_state] = 1

        q = deque([(sr, sc, E, 0, 0)])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while q:
            r, c, e, mask, dist = q.popleft()
            if e == 0:
                continue
            ne = e - 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    new_e = E if classroom[nr][nc] == 'R' else ne
                    lid = litter_id[nr][nc]
                    new_mask = mask | (1 << lid) if lid != -1 else mask
                    if new_mask == full_mask:
                        return dist + 1
                    state = encode(nr, nc, new_e, new_mask)
                    if not visited[state]:
                        visited[state] = 1
                        q.append((nr, nc, new_e, new_mask, dist + 1))

        return -1