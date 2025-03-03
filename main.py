from game import Game

def main():
    player_name = input("Введите имя игрока: ")
    computer_name = "Компьютер"
    game = Game(player_name, computer_name)
    game.start()

if __name__ == "__main__":
    main()
