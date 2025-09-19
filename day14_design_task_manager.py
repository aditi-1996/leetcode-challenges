import heapq
from typing import List, Tuple, Dict

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap: List[Tuple[int, int]] = []             # (−priority, −taskId)
        self.meta: Dict[int, Tuple[int, int]] = {}        # taskId -> (userId, priority)
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.meta[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.meta[taskId]
        self.meta[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))  # lazy update

    def rmv(self, taskId: int) -> None:
        if taskId in self.meta:
            del self.meta[taskId]  # heap entries skipped lazily

    def execTop(self) -> int:
        while self.heap:
            negp, negt = heapq.heappop(self.heap)
            taskId = -negt
            if taskId not in self.meta:
                continue
            userId, curp = self.meta[taskId]
            if -negp != curp:       # stale priority
                continue
            del self.meta[taskId]    # consume task
            return userId
        return -1