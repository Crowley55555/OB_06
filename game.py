import random
from hero import Hero

class Game:
    def __init__(self, player_name, computer_name):
        """
        Конструктор класса Game.

        Инициализирует новую игру с заданными именами для игрока и компьютера.
        Создает экземпляры класса Hero для игрока и компьютера.

        :param player_name: Имя игрока, строка
        :param computer_name: Имя компьютера, строка
        """
        self.player = Hero(player_name)  # Создает героя для игрока
        self.computer = Hero(computer_name)  # Создает героя для компьютера

    def start(self):
        """
        Метод для запуска игры.

        Чередует ходы между игроком и компьютером, пока один из героев не умрет.
        Выводит информацию о каждом ходе и объявляет победителя в конце игры.
        """
        turn = 0  # Счетчик ходов
        # Основной игровой цикл
        while self.player.is_alive() and self.computer.is_alive():
            turn += 1
            print(f"\nХод {turn}:")
            # Чередуем ходы между игроком и компьютером
            if turn % 2 == 1:
                self.player_turn()
            else:
                self.computer_turn()

            self.show_status()  # Выводим текущий статус игроков

        self.declare_winner()  # Объявляем победителя

    def player_turn(self):
        """
        Метод для хода игрока.

        Позволяет игроку выбрать оружие для атаки и атаковать компьютера.
        """
        # Запрашиваем у пользователя выбор оружия
        weapon = input("Игрок атакует! Выберите оружие (sword/bow) или нажмите Enter для стандартной атаки: ")
        # Игрок атакует компьютера с выбранным оружием
        self.player.attack(self.computer, weapon.lower() if weapon else None)

    def computer_turn(self):
        """
        Метод для хода компьютера.

        Компьютер случайным образом выбирает оружие и атакует игрока.
        """
        # Компьютер случайно выбирает оружие
        weapon = random.choice(["sword", "bow", None])
        print(f"Компьютер атакует с помощью {weapon if weapon else 'кулаков'}!")
        # Компьютер атакует игрока с выбранным оружием
        self.computer.attack(self.player, weapon)

    def show_status(self):
        """
        Метод для вывода статуса игроков.

        Выводит текущее здоровье игрока и компьютера после каждого хода.
        """
        print(f"Здоровье игрока: {self.player.health}")
        print(f"Здоровье компьютера: {self.computer.health}")

    def declare_winner(self):
        """
        Метод для объявления победителя.

        Проверяет, кто из героев остался в живых, и объявляет его победителем.
        """
        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Компьютер победил!")
