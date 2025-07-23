from src.hero import Hero
from src.enemy import Enemy

def main():
    hero = Hero(
        name='Heroi', 
        health=100, 
        level=5, 
        special_ability='Super Força'
    )
    print(hero.show_details())
    enemy = Enemy(
        name='Inimigo',
        health=80,
        level=3,
        type='Goblin'
    )
    print(enemy.show_details())
    

if __name__ == "__main__":
    main()