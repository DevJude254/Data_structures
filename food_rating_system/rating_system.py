import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_info = {}

        self.cuisine_map = {}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heapq.heappush(self.cuisine_map[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating

        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_map[cuisine]

        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap) 

 # sample
foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
cuisines = ["korean","japanese","japanese","greek","japanese","korean"]
ratings = [9,12,8,15,14,7]

fr = FoodRatings(foods, cuisines, ratings)

print(fr.highestRated("korean"))   
print(fr.highestRated("japanese"))
fr.changeRating("sushi", 16)
print(fr.highestRated("japanese")) 
fr.changeRating("ramen", 16)
print(fr.highestRated("japanese")) 
