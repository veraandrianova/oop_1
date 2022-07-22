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
class Room:
    def __init__(self):
        self.all = {1: 'свободно', 2: 'свободно', 3: 'свободно'}
        self.free = [1, 2, 3]


class Rooms:
    ALL_ROOMS = {1: 'свободно', 2: 'свободно', 3: 'свободно'}

    def __init__(self):
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
# h = Hotels(3)
# r = Rooms(h.get_count_rooms())
# print(r.take_room_choose(3))
class Human():
    DICTS = {}

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_info(cls):
        return cls.DICTS

    def get_number(self, room):
        self.room = room
        self.DICTS[self.name] = self.room
        return self.DICTS

    def cheak_leaving(self):
        for k, v in self.DICTS.items():
            if self.name == k:
                return v

    def leaving(self):
        self.number = self.cheak_leaving()
        del self.DICTS[self.name]
        return self.DICTS

class Hotel:

    def __init__(self):
        self.room = Rooms()

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
            return self.name.get_info()
        else:
            return False


h = Hotel()
print(h.get_state())
print(h.get_free_rooms())
print(h.register_person('jack'))
print(h.take_non_choose_room())
print(h.get_state())
print(h.take_choose_room(2))
print(h.get_state())
print(h.get_free_rooms())
print(h.take_choose_room(2))
#
# while True:
#     action = input('Выберите действие: 1 посмотреть номерной фонд 2 посмотреть свободные номера, 3 заселить/выселить 4 сменить статус номера - на ремонте 5 список постояльцев')
#     h = Hotels(3)
#     r = Rooms(h.get_count_rooms())
#     if action == "1":
#         print(r.get_rooms())
#     elif action == '2':
#         print(r.status_free())
#     elif action == '3':
#         name = input("Введите имя: ")
#         action_2 = input("Выберите действие: 1 заселить 2 выселить ")
#         h = Human(name)
#         print(action_2)
#         if action_2 == '1':
#             action_3 = input("Предоставить выбор номера? да/нет ")
#             if action_3 == 'нет':
#                 room = r.take_room()
#                 print(room)
#                 print(r.status_free())
#                 print(r.get_rooms())
#                 print(h.get_number(room))
#                 print(h.get_info())
#                 print(r.change_status_occupied(room))
#
#             if action_3 == 'да':
#                 print(r.get_rooms())
#                 action_4 = int(input("Введите номер: "))
#                 free = r.status_free()
#                 if action_4 in free:
#                     room = r.take_room_choose(action_4)
#                     print(room)
#                     print(r.status_free())
#                     print(r.get_rooms())
#                     print(h.get_number(room))
#                     print(h.get_info())
#         elif action_2 == '2':
#             room_number = h.cheak_leaving()
#             print(h.cheak_leaving())
#             print(h.leaving())
#             print(r.change_status_free(room_number))
#
#     elif action == '4':
#         print(r.status_free())
#         free = r.status_free()
#         action_5 = int(input(f"Введите номер комнаты: {free}"))
#         if action_5 in free:
#             print(r.change_status_repear(action_5))
#         else:
#             print(f'{action_5} не модет встать на ремонт он занят')
#
#     elif action == '5':
#         print(Human.get_info())
#

            



