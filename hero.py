import random

class Hero:
    def __init__(self, name):
        """
        Конструктор класса Hero.

        Инициализирует нового героя с заданным именем, начальным здоровьем и силой атаки.

        :param name: Имя героя, строка
        """
        self.name = name  # Имя героя
        self.health = 100  # Начальное здоровье героя
        self.attack_power = 20  # Сила атаки героя

    def attack(self, other, weapon=None):
        """
        Метод для атаки другого героя.

        Этот метод позволяет текущему герою атаковать другого героя, уменьшая его здоровье.
        Урон зависит от выбранного оружия.

        :param other: Экземпляр класса Hero, которого атакуют
        :param weapon: Тип оружия для атаки (sword/bow). Если не указано, используется стандартный урон.
        """
        # Определяем урон в зависимости от выбранного оружия
        if weapon == "sword":
            damage = random.randint(15, 25)  # Урон мечом
        elif weapon == "bow":
            damage = random.randint(10, 20)  # Урон луком
        else:
            damage = random.randint(10, 30)  # Стандартный урон

        # Уменьшаем здоровье атакуемого героя на величину урона
        other.health -= damage

        # Выводим информацию об атаке
        print(f"{self.name} наносит {damage} урона {other.name} с помощью {weapon if weapon else 'кулаков'}!")

    def is_alive(self):
        """
        Метод для проверки, жив ли герой.

        Возвращает True, если здоровье героя больше 0, иначе False.

        :return: True, если герой жив, иначе False
        """
        return self.health > 0