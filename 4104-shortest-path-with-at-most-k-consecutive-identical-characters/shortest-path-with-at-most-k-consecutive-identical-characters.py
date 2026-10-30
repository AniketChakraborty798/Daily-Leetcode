import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        INF = float('inf')
        dist = [INF] * (n * K)
        dist[0 * K + 1] = 0
        pq = [(0, 0, 1)]  # (cost, node, run)

        while pq:
            d, u, r = heapq.heappop(pq)
            if d > dist[u * K + r]:
                continue
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                nr = r + 1 if labels[v] == lu else 1
                if nr > k:
                    continue
                nd = d + w
                idx = v * K + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(pq, (nd, v, nr))

        return -1