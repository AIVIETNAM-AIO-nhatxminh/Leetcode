from typing import List
import sys

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find(self, i) -> int:
        if self.parent[i] == i:
            return self.parent[i]
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[y_root] > self.rank[x_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
            return True
        return False 

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        result = sys.maxsize
        union = UnionFind(100000)

        for road in roads:
            union.union(road[0], road[1])

        for road in roads:
            if union.find(1) == union.find(road[0]) or union.find(1) == union.find(road[1]):
                result = min(result, road[2]) 
        return result