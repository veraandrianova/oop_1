# РЕАЛИЗОВАТЬ  МИКРО ФРЕЙМВОРК ПО МОДЕЛИ MVC. принять два вида запроса запись и чтение. при чтении выводить информацию
# о пользователе инф имя номер тел и мэйл. при записи принимать имя тел мэйл. и сохранять их и вернуть ответ что все хорошо
import json


class Save:
    # сохраняет
    def __init__(self, mobil, name, email):
        self.mobil = mobil
        self.name = name.lower()
        self.email = email

    def cheack_mobil(self):
        mobil_list = []
        with open('data.txt', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for i in data:
                if i['mobil'] == self.mobil:
                    mobil_list.append(self.mobil)
            if len(mobil_list) > 0:
                return False
            else:
                self.save()
                return True

    def save(self):
        entry = {}
        entry['mobil'] = self.mobil
        entry['name'] = self.name
        entry['email'] = self.email
        with open('data.txt', "r", encoding='utf-8') as file:
            data = json.load(file)
        data.append(entry)
        with open('data.txt', "w", encoding='utf-8') as file:
            json.dump(data, file)
        return True


class Read:
    # чтение
    def __init__(self, value):
        self.value = value.lower()

    def cheack_value(self):
        mobil_list = []
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for i in data:
                if i['mobil'] == self.value or i['name'] == self.value:
                    mobil_list.append(i)
            if len(mobil_list) == 0:
                return False
            else:
                return mobil_list


class Connector:

    def __init__(self, action):
        self.action = action

    def get_method(self):
        if self.action == '1':
            self.action_phone = input('Введите номер: ')
            self.action_name = input('Введите имя: ')
            self.action_email = input('Введите емаил: ')
            return self.action_phone, self.action_name, self.action_email
        if self.action == '2':
            self.action_value = input('Введите данные для поиска: ')
            return self.action_value

    def view(self, args):
        self.args = args
        print('Имя - номер - почта')
        for i in self.args:
            print(i['name'], i['mobil'], i['email'])


    def read(self, *args):
        self.args = args
        if len(self.args) == 1:
            self.reader = Read(self.args[0])
            self.reader = Read(self.args[0])
            if not self.reader.cheack_value():
                return False
            else:
                self.reader_search = tuple(self.reader.cheack_value())
                self.view(self.reader_search)
                return True
        else:
            return False

    def to_save(self, args):
        self.args = args
        self.mobil = self.args[0]
        self.name = self.args[1]
        self.email = self.args[2]
        self.saved = Save(self.mobil, self.name, self.email)
        self.result = self.saved.cheack_mobil()
        if self.result:
            self.read(self.mobil)
            return True
        else:
            self.read(self.mobil)
            return False



while True:
    action = input('Выберите действие: 1 запись, 2 чтение')
    c = Connector(action)
    if action == '1':
        result = c.to_save(c.get_method())
        if result:
            print('Абонент сохранен')
            print(result)
        else:
            print('Абонент существует')
            print(result)

    elif action == '2':
        result = c.read(c.get_method())
        if result:
            print(result)
        else:
            action_1 = input('Данного абонента нет в списке, хотите его внести да/нет:')
            if action_1 == 'да':
                c = Connector('1')
                result_1 = c.to_save(c.get_method())
                if result_1:
                    print('Абонент сохранен')
                    print(result_1)
                else:
                    print('Абонент существует')
                    print(result_1)

