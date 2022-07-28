class Rooms:
    ALL_ROOMS = {1: 'свободно', 2: 'занято', 3: 'на ремонте'}

    def __init__(self, number):
        self.number = number
        self.status = 'свободно'


class Human:
    DICTS = {}

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_info(cls):
        sorted_tuple = sorted(cls.DICTS.items(), key=lambda x: x[0])
        cls.DICTS = dict(sorted_tuple)
        return cls.DICTS

    def get_number(self, room):
        self.room = room
        self.DICTS[self.room] = self.name
        return self.DICTS

    def cheak_leaving(self, room_number):
        self.room_number = int(room_number)
        print(self.DICTS[self.room_number])
        if self.DICTS[self.room_number] == self.name:
            print(self.DICTS[self.room_number])
            return self.room_number
        else:
            return False

    def leaving(self, number):
        self.room_number_leaving = number
        del self.DICTS[self.room_number_leaving]
        return self.DICTS


class Hotel:

    def __init__(self, count_room):
        self.rooms = [Rooms(i) for i in range(1, count_room + 1)]

    def change_status_repair(self, number_room):
        self.number = number_room
        for room in self.rooms:
            if room.number == self.number:
                print(room.number)
                if room.status == 'свободно' and room.status != 'занято':
                    room.status = 'на ремонте'
                    return True
                else:
                    return False

    def register_person(self, name):
        self.name = Human(name)
        return self.name.name

    def get_status_room_all(self):
        for room in self.rooms:
            print(f"Номер: {room.number} - {room.status}")

    def take_choose_room(self, cur_number):
        self.cur_number = cur_number
        for room in self.rooms:
            if room.number == self.cur_number:
                if room.status == 'свободно':
                    room.status = 'занято'
                    self.name.get_number(self.cur_number)
                    return Human.get_info()
                else:
                    return False

    def free_room_after_occupied(self, cur_number):
        self.cur_number = cur_number
        for room in self.rooms:
            if room.number == int(self.cur_number):
                if room.status != 'свободно':
                    room.status = 'свободно'
                    return True
                return False

    def free_room(self, cur_number):
        self.cur_number = cur_number
        for room in self.rooms:
            if room.number == self.cur_number:
                print(room.number)
                if room.status != 'свободно' and room.status != 'занято':
                    room.status = 'свободно'
                    print(room.status)
                    return True
                return False

    def cheack_out(self, room):
        self.number = room
        self.room_number = self.name.cheak_leaving(self.number)
        if self.room_number:
            print(self.room_number)
            print(self.name.leaving(self.room_number))
            print(self.free_room_after_occupied(self.number))
            return 'ok'
        else:
            return False

    def take_non_choose_room(self):
        self.free_rooms = []
        for room in self.rooms:
            if room.status == 'свободно':
                self.free_rooms.append(room)
        self.free_rooms[0].status = 'занято'
        self.name.get_number(self.free_rooms[0].number)
        return self.name.get_info()

    def get_free_rooms(self):
        self.free_rooms = []
        for room in self.rooms:
            if room.status == 'свободно':
                self.free_rooms.append(room.number)
        return self.free_rooms


numbers = int(input('Сколько комнат в отеле? '))
h = Hotel(numbers)

while True:
    action = input(
        '''Выберите действие:
        1 посмотреть номерной фонд
        2 посмотреть свободные номера,
        3 заселить/выселить
        4 сменить статус номера
        5 список постояльцев''')

    if action == "1":
        print(h.get_status_room_all())
    elif action == '2':
        print(h.get_free_rooms())
    elif action == '3':
        action_2 = input("Выберите действие: 1 заселить 2 выселить ")
        print(action_2)
        if action_2 == '1':
            name = input("Введите имя: ")
            print(h.register_person(name))
            action_3 = input("Предоставить выбор номера? да/нет ")
            if action_3 == 'нет':
                print(h.take_non_choose_room())
            if action_3 == 'да':
                action_4 = int(input("Введите номер: "))
                if h.take_choose_room(action_4):
                    print(Human.get_info())
                else:
                    print("Выберите комнату из свободных:")
                    print(h.get_free_rooms())
        elif action_2 == '2':
            room = input("Введите номер комнаты: ")
            name = input("Введите имя: ")
            h.register_person(name)
            try:
                if h.cheack_out(room):
                    print(h.cheack_out(room))
                    print(Human.get_info())
                else:
                    print(f'Проверьте соотвествие комнаты и постояльца')
            except:
                print(f'Проверьте соотвествие комнаты и постояльца')
    elif action == '4':
        action_5 = int(input(f"Введите номер комнаты: "))
        action_7 = int(input(f"Установить статус 1 свободен 2 на ремонте: "))
        if action_7 == 2:
            if h.change_status_repair(action_5):
                print(h.get_status_room_all())
            else:
                print(f'{action_5} не может встать на ремонт он занят')
        elif action_7 == 1:
            if h.free_room(action_5):
                print(h.get_status_room_all())
            else:
                print(f'{action_5} не может встать встать на свободен он не был на ремонте')

    elif action == '5':
        print(Human.get_info())
