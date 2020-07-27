"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты\
обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число,\
то игроки перебрасывают кубики.
"""

import random


def dice():
    return random.randint(1, 6)


def compare_dice(plr_1, plr_2):
    if plr_1 == plr_2:
        return None
    return plr_1 > plr_2


player_1_score = 0
player_2_score = 0
attempts = 0

print("The dices game\n")
while attempts < 10:
    player_1_dice = dice()
    player_2_dice = dice()
    print(f"dices: {player_1_dice} - {player_2_dice}")
    var = compare_dice(player_1_dice, player_2_dice)

    if var is None:
        continue
    if var is True:
        player_1_score += 1
        attempts += 1
    elif var is False:
        player_2_score += 1
        attempts += 1
    if attempts == 10 and player_1_score == player_2_score:
        attempts -= 1

    print(f"Attempts: {attempts} | Score: {player_1_score} -\
    {player_2_score}\n")

else:
    win = compare_dice(player_1_score, player_2_score)
    if win:
        print("\nFirst player Win")
    else:
        print("\nSecond player Win")
