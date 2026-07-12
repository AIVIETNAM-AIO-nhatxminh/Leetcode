from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.nodes: list[int] = [1] * size
        self.edges: list[int] = [0] * size
    
    def find(self, i) -> int:
        if self.parent[i] == i:
            return self.parent[i]
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.nodes[x_root] > self.nodes[y_root]:
                self.nodes[x_root] += self.nodes[y_root]
                self.edges[x_root] += self.edges[y_root] + 1
                self.parent[y_root] = x_root
            elif self.edges[y_root] > self.edges[x_root]:
                self.nodes[y_root] += self.nodes[x_root]
                self.edges[y_root] += self.edges[x_root] + 1
                self.parent[x_root] = y_root
            else:
                self.nodes[x_root] += self.nodes[y_root]
                self.edges[x_root] += self.edges[y_root] + 1
                self.parent[y_root] = x_root
        else:
            self.edges[x_root] += 1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        result = 0

        for edge in edges:
            uf.union(edge[0], edge[1])

        unique_parent = set(uf.parent)
        print(uf.parent)
        print(unique_parent)
        print(uf.nodes)
        print(uf.edges)

        for node in unique_parent:
            n = uf.nodes[uf.find(node)]
            if (n * (n - 1)) / 2 == uf.edges[node]:
                result += 1
        return result
    
if __name__ == "__main__":
    solution = Solution()
    n = 4
    edges = [[2,0],[3,1],[3,2]]
    print(solution.countCompleteComponents(n, edges))