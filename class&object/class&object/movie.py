class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

movie1 = Movie("Movie A", "Hero A", "Heroine A", 4.5)
movie2 = Movie("Movie B", "Hero B", "Heroine B", 4.0)

print("Movie 1")
print("Movie Name:", movie1.name)
print("Hero:", movie1.hero)
print("Heroine:", movie1.heroine)
print("Rating:", movie1.rating)

print("\nMovie 2")
print("Movie Name:", movie2.name)
print("Hero:", movie2.hero)
print("Heroine:", movie2.heroine)
print("Rating:", movie2.rating)