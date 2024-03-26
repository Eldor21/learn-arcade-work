class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def meow(self):
        print(self.name + " says: Meow!")


my_cat = Cat("Tom", "Grey", 5.5)
my_cat.meow()


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(self.name + " died!")


my_monster = Monster("Goblin", 60)
my_monster.decrease_health(70)
