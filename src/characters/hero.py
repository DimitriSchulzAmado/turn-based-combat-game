from src.characters.character import Character


class Hero(Character):
    def __init__(self, name, health, level, special_ability):
        super().__init__(name, health, level)
        self.__special_ability = special_ability

    def get_special_ability(self):
        return self.__special_ability

    def show_details(self):
        details = super().show_details()
        return f"{details} \
                \nSpecial Ability: {self.get_special_ability()}"

    def special_attack(self, target):
        damage = self.get_level() * 5
        print(
            f"{self.get_name()} uses special attack on {target.get_name()} for {damage} damage!"
        )
