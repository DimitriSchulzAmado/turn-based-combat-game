from src.characters.character import Character


class Enemy(Character):
    def __init__(self, name, health, level, type):
        super().__init__(name, health, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        details = super().show_details()
        return f"{details} \
                \nType: {self.get_type()}"
