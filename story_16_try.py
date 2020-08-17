"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.
Что делать дома:
    - реализовать конвертацию c различных валют в гривну при добалении денег в банкомат и при снятии
"""
from dataclasses import dataclass


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
        self.currency = 'UAH'
        self.curr_map = {'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, valoe):
        self.initial_amount += ...

    def withdraw(self, amount):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        self.initial_amount -= amount
        return amount


"""
Нужно дописать основную линию сказки. Каждого героя реализовать классом с методами. 
Так же должен быть класс сказки (или функция), где происходит основное действие с героями
"""


# ___________KOLOBOK_______________


class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    def appear_colobok(self):
        colobok = True
        return colobok
        
    def escape_from_home(self):
        text = "\nRun Forest, run"
        return print(text)


class Babka(Hero):
    def bake_colobok(self):
        text ='\nПошла Бабка по сусекам помела, по коробкам поскребла \nи набрала муки горстку. \nИспекла Колобок да на окошко студить поставила.'
        
        return print(text) # Colobok

class Ded(Hero):
    def tell_babka_about_colobok(self):
        text = 'Вот Дед и говорит Бабке: "Ты бы, Бабка, по сусекам помела,\nпо коробкам поскребла. Авось муки и наберётся.\nДа испеки колобок.'
        return print(text)



class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None
        
    @staticmethod
    def intro():
        text = "Жили были дед да баба и не было у них ни хлеба,\n ни соли, ни кислых щей.\n"
        return print(text)
    
    @staticmethod
    def while_cooking_colobok():
        text = " "
        return print (text)
        
        
    def babkin_dom(self):
        self.ded.tell_babka_about_colobok(self.babka)
       # self.colobok = self.babka.bake_colobok(self.colobok)

    def start(self):
        self.babkin_dom()

#Main
my_tail = Tale(Babka, Ded)

Tale.intro()
my_tail.start()

Babka.bake_colobok(Colobok)

Colobok.escape_from_home(Colobok.appear_colobok)
