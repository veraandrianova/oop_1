# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве
# аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
# Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде
# с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random


import random


class Unit:
    def __init__(self, number, commandid):
        self.number = number
        self.commandId = commandid


class Hero(Unit):
    def __init__(self,  number, commandid, name, level=1):  # При инициализации добавляем свойства name и level
        Unit.__init__(self, number, commandid)
        self.name = name  # Привязываем классу Hero свойство level и name
        self.level = level

    def getlevel(self):
        return self.level

    def inclevel(self):
        self.level += 1
        print('Уровень героя', self.name,'увеличен на 1 и равен', self.level)


class Soldier(Unit):
    def gotohero(self, Hero):
        print('Солдат номер', self.number, 'следует за героем', Hero.name, 'с номером', Hero.number)


H1 = Hero(1, 1, 'Arthas')  # Создаем героев с номерами 1 и 2
H2 = Hero(2, 2, 'Illidan')
armyH1, armyH2 = [], []  # Списки солдат

for i in range(3, 10):  # Генерим нечетное количество солдат
    n = random.randint(0, 1)
    if n:
        armyH1.append(Soldier(i, 1))
        print('Солдат с номером', i, 'добавлен в армию', H1.name)
    else:
        armyH2.append(Soldier(i, 2))
        print('Солдат с номером', i, 'добавлен в армию', H2.name)

print('Армия героя', H1.name, ':', len(armyH1))
print('Армия героя', H2.name, ':', len(armyH2))

if len(armyH1) > len(armyH2):
    print('В армии', H1.name, 'больше солдат, увеличиваем его уровень')
    H1.inclevel()
else:
    print('В армии', H2.name, 'больше солдат, увеличиваем его уровень')
    H2.inclevel()

armyH1[1].gotohero(H2)
