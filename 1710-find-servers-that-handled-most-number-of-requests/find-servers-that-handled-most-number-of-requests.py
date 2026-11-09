import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Free servers are stored as "virtual ids" >= current i, so a plain
        # min-heap gives the first free server at or after i % k (with wraparound).
        free = list(range(k))          # virtual ids 0..k-1
        heapq.heapify(free)
        busy = []                      # (end_time, virtual_id)
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            # Release servers that finished by now.
            while busy and busy[0][0] <= start:
                _, vid = heapq.heappop(busy)
                # Shift to the next virtual id >= i that maps to the same real server.
                nxt = i + ((vid - i) % k)
                heapq.heappush(free, nxt)

            if not free:
                continue               # all busy, drop request

            vid = heapq.heappop(free)
            server = vid % k
            count[server] += 1
            heapq.heappush(busy, (start + dur, vid))

        mx = max(count)
        return [s for s, c in enumerate(count) if c == mx]