import random

class Hero:
    def __init__(self, name):
        """
        Инициализация героя.

        :param name: Имя героя
        """
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other, weapon=None):
        """
        Атака другого героя с выбором оружия.

        :param other: Экземпляр класса Hero, которого атакуют
        :param weapon: Тип оружия для атаки (sword/bow)
        """
        if weapon == "sword":
            damage = random.randint(15, 25)  # Урон мечом
        elif weapon == "bow":
            damage = random.randint(10, 20)  # Урон луком
        else:
            damage = random.randint(10, 30)  # Стандартный урон

        other.health -= damage
        print(f"{self.name} наносит {damage} урона {other.name} с помощью {weapon if weapon else 'кулаков'}!")

    def is_alive(self):
        """
        Проверка, жив ли герой.

        :return: True, если здоровье больше 0, иначе False
        """
        return self.health > 0
