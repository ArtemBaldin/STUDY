"""
Реализовать класс Person, у которого должно быть два атрибута: age и name.
Также у него должен быть следующий набор методов:
def know(self, another_person_object)
который позволяет добавить другого человека в список знакомых\
(лист __friends (обязательно приватный атрибут)).
И метод
def is_known(self, another_person_object)
который возвращает знакомы ли два человека (True/False)
"""


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.__know_list = []

    def know(self, another_person_object):
        self.__know_list.append(another_person_object)

    def is_known(self, another_person_object):
        if another_person_object in self.__know_list:
            return True
        else:
            return False


pers_1 = Person(20, "Ivan")
pers_2 = Person(25, "Max")
pers_3 = Person(22, "Luck")
pers_4 = Person(30, "Sky")

pers_1.know(pers_4)
print(f"pers_1 --> pers_4: {pers_1.is_known(pers_4)}")
print(f"pers_1 --> pers_3: {pers_1.is_known(pers_3)}")
print(f"pers_4 --> pers_1: {pers_4.is_known(pers_1)}")
