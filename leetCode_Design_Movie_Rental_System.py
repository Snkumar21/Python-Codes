import heapq
from collections import defaultdict

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.price_map = {}   # (shop, movie) -> price
        self.unrented = defaultdict(list)  # movie -> min-heap of (price, shop)
        self.rented = []      # min-heap of (price, shop, movie)

        self.unrented_set = set()
        self.rented_set = set()

        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            heapq.heappush(self.unrented[movie], (price, shop))
            self.unrented_set.add((shop, movie))

    def search(self, movie):
        result = []
        seen = set()
        temp = []

        while self.unrented[movie] and len(result) < 5:
            price, shop = heapq.heappop(self.unrented[movie])
            if (shop, movie) in self.unrented_set and shop not in seen:
                result.append(shop)   # ✅ only shop ID
                seen.add(shop)
            temp.append((price, shop))

        # restore heap
        for item in temp:
            heapq.heappush(self.unrented[movie], item)

        return result

    def rent(self, shop, movie):
        price = self.price_map[(shop, movie)]
        self.unrented_set.discard((shop, movie))
        self.rented_set.add((shop, movie))
        heapq.heappush(self.rented, (price, shop, movie))

    def drop(self, shop, movie):
        price = self.price_map[(shop, movie)]
        self.rented_set.discard((shop, movie))
        self.unrented_set.add((shop, movie))
        heapq.heappush(self.unrented[movie], (price, shop))

    def report(self):
        result = []
        temp = []

        while self.rented and len(result) < 5:
            price, shop, movie = heapq.heappop(self.rented)
            if (shop, movie) in self.rented_set:
                result.append([shop, movie])  # ✅ correct format
            temp.append((price, shop, movie))

        # restore heap
        for item in temp:
            heapq.heappush(self.rented, item)

        return result