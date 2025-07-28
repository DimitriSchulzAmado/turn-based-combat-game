from src.characters.hero import Hero
from src.characters.enemy import Enemy


class Game:
    """The game's orchestrating class."""

    def __init__(self):
        self.hero = Hero(
            name="Heroi", health=100, level=5, special_ability="Super Força"
        )
        self.enemy = Enemy(name="Inimigo", health=80, level=5, type="Goblin")

    def start_battle(self):
        print("Battle starting!")

        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("Characters details:")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Press Enter to attack...")
            choice = input("Choose your action (1: Attack, 2: Special Attack):")

            match choice:
                case "1":
                    self.hero.attack(self.enemy)
                case "2":
                    self.hero.special_attack(self.enemy)
                case _:
                    print("Invalid choice, try again.")
                    continue

            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print("Congratulations. Hero wins!")
        else:
            print("Enemy wins!")
