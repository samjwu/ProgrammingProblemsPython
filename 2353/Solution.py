class Food:
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name
        
        return self.rating > other.rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating_dict = {}
        self.cuisine_dict = {}
        self.max_heap = defaultdict(list)

        n = len(foods)
        for i in range(n):
            self.rating_dict[foods[i]] = ratings[i]
            self.cuisine_dict[foods[i]] = cuisines[i]
            heapq.heappush(self.max_heap[cuisines[i]], Food(foods[i], ratings[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating_dict[food] = newRating
        heapq.heappush(self.max_heap[self.cuisine_dict[food]], Food(food, newRating))

    def highestRated(self, cuisine: str) -> str:
        best_food = self.max_heap[cuisine][0]

        # get rid of old values in heap
        while self.rating_dict[best_food.name] != best_food.rating:
            heapq.heappop(self.max_heap[cuisine])
            best_food = self.max_heap[cuisine][0]

        return best_food.name
