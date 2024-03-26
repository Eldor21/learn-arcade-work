class Star:
    def __init__(self, name):
        self.get_name = name
        print("A star is born! It's name is" + name)
    def get_name(self):
        print("A star is born! It's name is" + name)
star1 = Star(" Zuxro")
star2 = Star(" Mars")
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

monster1 = Monster("Godzilla", 100)
monster2 = Monster("Monkey_King", 75)

print(monster1.name, "has health:", monster1.health)
print(monster2.name, "has health:", monster2.health)
