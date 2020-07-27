from logic import run_wheel
from logic import convert_data
from logic import player_score
from logic import validate_game


def game_start():
    print("Slot machine game\n")

    total_score = 0
    game = True

    print("Are You ready?\nGo!")
    while game is True:
# можно дописать дополнитенльную запускалку
        show_comb = run_wheel()
        print(f"\n{show_comb}")

        game_round = player_score \
            (convert_data(show_comb))
        total_score += game_round
        print(f"Score: {game_round}\nTotal score: {total_score}\n")

        game =None
        while game == None:
            game =validate_game(input("Would You like to continue?[Y/N]"))

    else:
        print(f"\nTotal score is: {total_score}\n")

if __name__ == '__main__':
    game_start()