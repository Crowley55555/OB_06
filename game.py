import random
from hero import Hero

class Game:
    def __init__(self, player_name, computer_name):
        """
        Инициализация игры.

        :param player_name: Имя игрока
        :param computer_name: Имя компьютера
        """
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """
        Запуск игры. Чередует ходы между игроком и компьютером,
        пока один из героев не умрет.
        """
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            turn += 1
            print(f"\nХод {turn}:")
            if turn % 2 == 1:
                self.player_turn()
            else:
                self.computer_turn()

            self.show_status()

        self.declare_winner()

    def player_turn(self):
        """
        Ход игрока с выбором оружия.
        """
        weapon = input("Игрок атакует! Выберите оружие (sword/bow) или нажмите Enter для стандартной атаки: ")
        self.player.attack(self.computer, weapon.lower() if weapon else None)

    def computer_turn(self):
        """
        Ход компьютера со случайным выбором оружия.
        """
        weapon = random.choice(["sword", "bow", None])
        print(f"Компьютер атакует с помощью {weapon if weapon else 'кулаков'}!")
        self.computer.attack(self.player, weapon)

    def show_status(self):
        """
        Вывод статуса игроков.
        """
        print(f"Здоровье игрока: {self.player.health}")
        print(f"Здоровье компьютера: {self.computer.health}")

    def declare_winner(self):
        """
        Объявление победителя.
        """
        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Компьютер победил!")
