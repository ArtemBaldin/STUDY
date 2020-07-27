import random


def run_wheel():
    wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
    wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]

    def rand_wheel():
        return random.randint(0, 9)

    return wheel1[rand_wheel()], wheel2[rand_wheel()], wheel3[rand_wheel()]


def convert_data(tupl: tuple):
    double_scores = False
    value_dic = {}
    if tupl.count("XXX") == 1:
        double_scores = True
    for k in tupl:
        if tupl.count(k) > 1:
            value_dic.setdefault(k, tupl.count(k))
    return value_dic, double_scores


def player_score(wheels: tuple):
    score_list = {"XXX": (100, 10, 100), \
                  "A": (90, 9, 18), \
                  "B": (80, 8, 16), \
                  "C": (70, 7, 14), \
                  "D": (60, 6, 12), \
                  "E": (50, 5, 10), \
                  "F": (40, 4, 8), \
                  "G": (30, 3, 6), \
                  "H": (20, 2, 4), \
                  "I": (10, 1, 2)}

    cons = 0
    total_scores = 0
    if wheels[1] is True:
        doub_score = 1
    else:
        doub_score = 0

    for k in wheels[0].keys():
        cons = wheels[0][k]
        total_scores = score_list[k][3 - cons + doub_score]

    return total_scores


def validate_game(string: str):
    if string.lower() == "y":
        string = True
    elif string.lower() == "n":
        string = False
    else:
        return None
    return string
