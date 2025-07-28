import random


class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Name: {self.get_name()} \
                \nHealth: {self.get_health()} \
                \nLevel: {self.get_level()}"

    def receive_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        print(f"{self.get_name()} now has {self.get_health()} health left.")

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_damage(damage)
        print(f"{self.get_name()} attacks {target.get_name()} for {damage} damage!")
