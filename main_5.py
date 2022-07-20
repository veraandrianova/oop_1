# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве
# аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
# Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде
# с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random


class Member:

    def __init__(self, number, command):
        self.number = number
        self.command = command

    def get_member(self):
        return f'{self.number} {self.command}'


class Members:

    def __init__(self):
        number = '012345'
        command = '12'
        self.member = [Member(n, m) for m in command for n in number]
        random.shuffle(self.member)

    def get_members(self):
        return self.member.pop()
f = Members()
print(f.get_members)

class Hero:
    number = 0
    command = 0

    def __init__(self, number, command):
        self.number = number
        self.command = command

    def print_level(self):
        print(f'уровень у солдата{self.level}')

    def level(self):
        self.level += 1
        self.print_level()


class Soldier:
    number = 0
    command = 0

    def __init__(self, number, command):
        self.number = number
        self.command = command

    def go_to_hero(self, hero: Hero):
        self.hero = hero
        return f'Иду за {self.hero}'


class Players:

    def __init__(self, member):
        self.member = member
        self.firs_command = []
        self.second_command = []

    @property
    def get_command(self):
        return f'{self.firs_command}, {self.second_command}'

    @get_command.setter
    def get_command(self, member: Member):
        if member.get_member()[1] == 0:
            self.firs_command.append(member)
        else:
            self.second_command.append(member)


class Play():

    def __init__(self, number_1, command_1, number_2, command_2):
        self.soldier = Members()
        self.hero_1 = Hero(number=number_1, command=command_1)
        self.hero_2 = Hero(number=number_2, command=command_2)
        self.command_1 = Players(member=command_1)
        self.command_2 = Players(member=command_2)

    def start(self):
        self.command_1.get_command = self.soldier.get_members()
        self.command_2.get_command = self.soldier.get_members()
        print(self.command_1.get_command, self.command_2.get_command)

game = Play(1,1,2,2)

