"""
Реализовать класс Банкомат, у которого есть баланс.\
 Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус\
 и не может обрабатывать отрицательные сумму.
Что делать дома:
    - реализовать конвертацию c различных валют в гривну\
 при добалении денег в банкомат и при снятии
"""
from decimal import Decimal as dc
from dataclasses import dataclass
print("\n\tFIRST TASK\n")


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 0
    max_limit = 0
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.max_limit = 1000
        self.currency = 'UAH'
        self.curr_map = {'UAH': 1, 'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, value, cur='UAH'):
        if cur == "USD" or cur == "EUR" or cur == "UAH":
            value = float(dc(str(value)) * dc(str(self.curr_map[cur])))
        else:
            return ValueError

        self.initial_amount += value
        return self.initial_amount

    def withdraw(self, amount, cur="UAH"):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        if cur == "USD" or cur == "EUR" or cur == "UAH":
            amount = float(dc(str(amount)) * dc(str(self.curr_map[cur])))
        else:
            return ValueError

        self.initial_amount -= amount
        return self.initial_amount


# MAIN
card = ATM(1000)
print(card.initial_amount)
card.add_money(100, "USD")
print(card.initial_amount)
print(card.withdraw(100, "EUR"))

"""
Нужно дописать основную линию сказки.\
Каждого героя реализовать классом с методами.
Так же должен быть класс сказки (или функция),\
где происходит основное действие с героями
"""

# ___________KOLOBOK_______________

print("\n\tSECOND TASK\n")


class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    def appear_colobok(self):
        colobok = True
        return colobok

    def escape_from_home(self):
        text = "\nНадоело Колобку на окне лежать,\
 он прыг с окна на лавку,\nс лавки на пол, прыг через порог на крыльцо,\
\nс крыльца во двор, со двора за ворота и был таков."
        return print(text)


class Babka(Hero):
    def bake_colobok(self):
        print(
            '\nПошла Бабка по сусекам помела, по коробкам поскребла\
\nи набрала муки горстку. \nИспекла Колобок да на окошко студить поставила.')

        return Colobok("Колобок")


class Ded(Hero):
    def tell_babka_about_colobok(self):
        text = 'Вот Дед и говорит Бабке: "Ты бы, Бабка,\
 по сусекам помела,\nпо коробкам поскребла.\
 Авось муки и наберётся.\nДа испеки колобок.'
        return text


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None

    def intro(self):
        text = "Жили были дед да баба и не было у них\
 ни хлеба,\nни соли, ни кислых щей.\n"
        return text

    def babkin_dom(self):
        print(self.ded.tell_babka_about_colobok(self.babka))
        self.colobok = self.babka.bake_colobok(self.colobok)
        self.colobok.escape_from_home()
        return "\nИ покатился по дорожке...\n"

    def start(self):
        self.intro()
        self.babkin_dom()


# Main
my_tail = Tale(Babka, Ded)
print(my_tail.intro())
print(my_tail.babkin_dom())
