from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        all_paths = []

        def dfs(node: int, path: List[int]):
            if node == target:
                all_paths.append(path.copy())
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # Backtrack

        dfs(0, [0]) 
        return all_paths