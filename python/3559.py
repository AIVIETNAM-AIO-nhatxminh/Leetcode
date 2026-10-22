from typing import List
from collections import deque

MOD = 10 ** 9 + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        length = len(edges) + 1
        graph = [[] for i in range(length + 1)]

        for _, edge in enumerate(edges):
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def bfs(self, node: int, target: int) -> int:
            arr = deque()
            visited = set()
            depth = 0
            curr_width = 0
            width_layer = [0 for i in range(length + 1)]
            width_layer[0] = 1 
            arr.append(node)

            while len(arr) > 0:
                curr = arr.popleft()
                if curr == target:
                    return depth
                curr_width += 1
                visited.add(curr)

                for edge in graph[curr]:
                    if edge not in visited:
                        width_layer[depth + 1] += 1
                        arr.append(edge)

                if curr_width == width_layer[depth]:
                    depth += 1
                    curr_width = 0      

            return depth   
        
        for _, query in enumerate(queries):
            result.append(int(2**(bfs(self, query[0], query[1]) - 1)) % MOD)
        return result
    

if __name__ == "__main__":
    solution = Solution()
    edges = [[1,2],[1,3],[3,4],[3,5]] 
    queries = [[1,4],[3,4],[2,5]]
    print(solution.assignEdgeWeights(edges, queries))