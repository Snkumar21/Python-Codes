import heapq

class TaskManager:
    def __init__(self, tasks):
        self.heap = []  # max-heap (simulate with negative values)
        self.task_map = {}  # taskId -> (userId, priority)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self):
        while self.heap:
            priority, negTaskId, userId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                curUser, curPriority = self.task_map[taskId]
                if curUser == userId and curPriority == -priority:
                    # valid task -> execute
                    del self.task_map[taskId]
                    return userId
        return -1