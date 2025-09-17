import heapq

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            # push (-rating, food) for max-heap
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))


    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        # push new rating into heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_to_heap[cuisine]
        # Clean up outdated ratings
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)  # discard outdated entry