class Hotels:
    status = {0: 'свободно', 1: 'на ремонте', 2: 'занято'}

    def __init__(self, count_rooms):
        self.count_rooms = count_rooms
        self.all_rooms = {}
        self.status_free_room = []
        self.status = 'свободно'

    def get_count_rooms(self):
        return self.count_rooms


h = Hotels(3)


class Rooms:
    ALL_ROOMS = {1: 'свободно', 2: 'свободно', 3: 'свободно'}

    def __init__(self, number):
        self.number = number

        self.status = 'свободно'
        self.choose_room = 0
        self.free_rooms = self.status_free()

    def get_rooms(self):
        return self.print_numbers()

    def status_free(self):
        self.status_free_room = []
        for k, v in self.ALL_ROOMS.items():
            if v == 'свободно':
                self.status_free_room.append(k)
        return self.status_free_room

    def change_status_occupied(self, index):
        self.ALL_ROOMS[index] = 'занято'
        return self.ALL_ROOMS

    def take_room(self):
        self.status_free_rooms = self.status_free()
        self.choose_room = self.status_free_rooms.pop()
        self.change_status_occupied(self.choose_room)
        return self.choose_room

    def take_room_choose(self, number):
        self.number = number
        self.status_free_rooms = self.status_free()
        self.status_free_rooms.remove(self.number)
        self.change_status_occupied(self.number)
        return self.status_free_rooms

    def change_status_free(self, index):
        self.ALL_ROOMS[index] = 'свободно'
        return self.ALL_ROOMS

    def change_status_repear(self, index):
        self.ALL_ROOMS[index] = 'на ремонте'
        return self.ALL_ROOMS

    def print_numbers(self):
        return self.ALL_ROOMS

    def print_free_numbers(self, number):
        self.number = number
        return self.number

    def cheak_repair(self, number):
        self.room_number_repair = int(number)
        print(self.ALL_ROOMS[self.room_number_repair])
        if self.ALL_ROOMS[self.room_number_repair] == 'на ремонте':
            print(self.ALL_ROOMS[self.room_number_repair])
            return self.room_number_repair
        else:
            return False


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
        self.rooms = [Rooms(i) for i in range(1, count_room+1)]

        self.room = Rooms()

    def change_status(self, status, number_room):
        for room in self.rooms:
            if room.number == number_room:
                room.status = status

    def get_status_room_all(self):
        for room in self.rooms:
            print(f"Номер: {room.number} - {room.status}")

    def get_state(self):
        return self.room.get_rooms()

    def get_free_rooms(self):
        return self.room.status_free()

    def register_person(self, name):
        self.name = Human(name)
        return self.name.name

    def take_non_choose_room(self):
        self_choose_room = self.room.take_room()
        self.room.get_rooms()
        self.name.get_number(self_choose_room)
        self.room.change_status_occupied(self_choose_room)
        return self.name.get_info()

    def take_choose_room(self, number):
        self.number = number
        self.free = self.room.status_free()
        if self.number in self.free:
            self.choose_room = self.room.take_room_choose(self.number)
            self.name.get_number(self.number)
            return Human.get_info()
        else:
            return False

    def cheack_out(self, room):
        self.number = room
        self.room_number = self.name.cheak_leaving(self.number)
        if self.room_number:
            self.name.leaving(self.room_number)
            return self.room.change_status_free(self.room_number)
        else:
            return False

    def status_for_repair(self, number):
        self.number_repair = number
        self.free = self.room.status_free()
        if self.number_repair in self.free:
            return self.room.change_status_repear(self.number_repair)
        else:
            return False

    def status_for_free(self, number):
        self.number_free = number
        self.cheeak_number_free = self.room.cheak_repair(self.number_free)
        if self.cheeak_number_free:
            self.room.change_status_free(self.number_free)
            return self.room.get_rooms()
        else:
            return False


numbers = input('Сколько комнат в ателе? ')
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
        print(h.get_state())
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
                    print(Human.get_info())
                else:
                    print(f'Проверьте соотвествие комнаты и постояльца')
            except:
                print(f'Проверьте соотвествие комнаты и постояльца')
    elif action == '4':
        action_5 = int(input(f"Введите номер комнаты: "))
        action_7 = int(input(f"Установить статус 1 свободен 2 на ремонте: "))
        if action_7 == 2:
            if h.status_for_repair(action_5):
                print(h.get_state())
            else:
                print(f'{action_5} не может встать на ремонт он занят')
        elif action_7 == 1:
            if h.status_for_free(action_5):
                print(h.get_state())
            else:
                print(f'{action_5} не может встать встать на свободен он не был на ремонте')

    elif action == '5':
        print(Human.get_info())
