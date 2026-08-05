class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        # Step 1: BFS from k to find suspicious methods
        suspicious = [False] * n
        suspicious[k] = True
        q = deque([k])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # Step 2: check no outside method invokes into the suspicious set
        for a, b in invocations:
            if suspicious[b] and not suspicious[a]:
                return list(range(n))  # cannot remove, return everything

        # Step 3: return the non-suspicious methods
        return [i for i in range(n) if not suspicious[i]]