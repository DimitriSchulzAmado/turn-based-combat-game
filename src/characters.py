class Personagem:
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