from characters import Personagem

class Hero(Personagem):
    def __init__(self, name, health, level, special_ability):
        super().__init__(name, health, level)
        self.__special_ability = special_ability

    def get_special_ability(self):
        return self.__special_ability
    
    def show_details(self):
        details = super().show_details()
        return f"{details} \
                \nSpecial Ability: {self.get_special_ability()}"