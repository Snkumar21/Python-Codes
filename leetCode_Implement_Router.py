from collections import deque, defaultdict
import bisect

class Router(object):
    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO storage of packets: [source, destination, timestamp]
        self.packetSet = set()  # For duplicate detection
        self.destMap = defaultdict(list)  # destination -> sorted timestamps list

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source, destination, timestamp)

        # Check duplicate
        if packet in self.packetSet:
            return False

        # If memory full, evict oldest
        if len(self.queue) >= self.memoryLimit:
            old_src, old_dest, old_time = self.queue.popleft()
            self.packetSet.remove((old_src, old_dest, old_time))
            # Remove timestamp from destMap[old_dest] (it's sorted)
            idx = bisect.bisect_left(self.destMap[old_dest], old_time)
            if idx < len(self.destMap[old_dest]) and self.destMap[old_dest][idx] == old_time:
                self.destMap[old_dest].pop(idx)
            if not self.destMap[old_dest]:
                del self.destMap[old_dest]

        # Add new packet
        self.queue.append(packet)
        self.packetSet.add(packet)
        bisect.insort(self.destMap[destination], timestamp)

        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))

        # Remove from destMap
        idx = bisect.bisect_left(self.destMap[destination], timestamp)
        if idx < len(self.destMap[destination]) and self.destMap[destination][idx] == timestamp:
            self.destMap[destination].pop(idx)
        if not self.destMap[destination]:
            del self.destMap[destination]

        return [source, destination, timestamp]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        if destination not in self.destMap:
            return 0

        times = self.destMap[destination]
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)
        return right - left
