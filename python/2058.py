# Definition for singly-linked list.
import sys
from ast import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points: list[int] = []
        curr = head
        prev = 0
        idx = -1
        minDistance = sys.maxsize

        while curr:
            idx += 1
            val = curr.val
            if prev != 0 and curr.next:
                if val < prev and val < curr.next.val:
                    if len(points) > 0:
                        minDistance = min(minDistance, idx - points[-1])
                    points.append(idx)
                if val > prev and val > curr.next.val:
                    if len(points) > 0:
                        minDistance = min(minDistance, idx - points[-1])
                    points.append(idx)
            curr = curr.next
            prev = val

        # print(points)
        if len(points) < 2:
            return [-1, -1]
        else: 
            return [minDistance, points[-1] - points[0]]
