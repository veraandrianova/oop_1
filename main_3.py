class Tomato:
    states = {0: 'Отсутствуе', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        return f'Томат на стадии {self._state}'


class TomatoBush:

    def __init__(self, count):
        self.tomatoes = []
        for i in range(0,count):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        total = []
        for i in self.tomatoes:
            if i.is_ripe():
                total.append(i)
        if len(total) == len(self.tomatoes):
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name, tomato: Tomato):
        self.name = name
        self._plant = tomato

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Садовник собирает урожай')
            self._plant.give_away_all()
        else:
            print('Не все плоды созрели')

    @staticmethod
    def knowledge_base():
        pass

t = TomatoBush(4)
g = Gardener('bob', t)
g.work()
g.work()
g.harvest()
g.work()
g.work()
g.harvest()
