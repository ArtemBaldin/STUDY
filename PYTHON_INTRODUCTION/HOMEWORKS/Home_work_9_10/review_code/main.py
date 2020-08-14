import random
from compare_value import compare_value
from validate_input import validate_input
from renew_game import renew_game


def start_game():
    print("Try to guess the digit.\n")
    game = True
    while game is True:
        random_number = random.randint(1, 1000)

        for i in range(10):
            print(f'У вас {10 - i} попыток!')
            player_select = validate_input(input('Введите число:'))
            if player_select is None:
                print("Error: You number is not correct!'")
                game = False
                break
            print(str(compare_value(random_number, player_select) + "\n"))
            if player_select == 'You win!!!!':
                break

        check = False
        while check is False and game is True or game is None:
            game = renew_game(input('Хотите прожолжить?[yes/no]'))
            if game is not None:
                check = True


if __name__ == '__main__':
    start_game()
