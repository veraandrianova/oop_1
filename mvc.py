import json


class Validator:

    def validator(self, *args, **kwargs):
        self.user = kwargs
        print(self.user)
        if len(self.user) == 1:
            return self.validator_phone()

        elif len(self.user) == 3:
            return self.validator_user()

    def validator_phone(self):
        phone = self.user.get('phone')
        if (len(phone) >= 11 and len(phone) <= 12) and (phone[0] == '+' or phone.isdecimal()):
            return True
        return False

    def validator_name(self):
        name = self.user.get('name')
        if (len(name) >= 2) and (name.isalpha()):
            return True
        return False

    def validator_email(self):
        email = self.user.get('email')
        if (len(email) >= 7) and ('@' in email) and ('.' in email):
            return True
        return False

    def validator_user(self):
        phone = self.validator_phone()
        name = self.validator_name()
        email = self.validator_email()
        if phone and name and email:
            return True
        return False


class Model:
    file = 'data.json'

    def filter(self, *args, **kwargs):
        data = self.read()
        for k, v in data.items():
            if k == kwargs.get('phone'):
                return k, v['name'], v['email']
        return False

    def read(self):
        with open(self.file, "r", encoding='utf-8') as file:
            return json.load(file)

    def save(self, *args, **kwargs):
        entry = self.read()
        data = {kwargs.get('phone'): {'name': kwargs.get('name'), 'email': kwargs.get('email')}}
        entry.update(data)
        with open(self.file, "w", encoding='utf-8') as file:
            json.dump(entry, file)
        return data


class View:

    def render(self, *args, **kwargs):
        total = f"{kwargs['phone']} - {kwargs['name']} - {kwargs['email']}"
        return total


class Controller:

    def get(self, *args, **kwargs):
        model = Model()
        validator = Validator()
        result = validator.validator(*args, **kwargs)
        if result:
            phone, name, email = model.filter(*args, **kwargs)
            if phone and name and email:
                return 200, View().render(phone=phone, name=name, email=email)
            else:
                return 400, False
        else:
            return 404, False

    def post(self, *args, **kwargs):
        model = Model()
        validator = Validator()
        result = validator.validator(*args, **kwargs)
        if result:
            if not model.filter(*args, **kwargs):
                user = model.save(*args, **kwargs)
                return 200, View().render(*args, **kwargs)
            else:
                phone, name, email = model.filter(*args, **kwargs)
                return 400, View().render(phone=phone, name=name, email=email)
        else:
            return 404, False


class Interface:

    def get(self):
        phone = input('Введите номер: ')
        name = input('Введите имя: ')
        email = input('Введите емаил: ')
        return phone, name, email

    def filter(self):
        return input('Введите номер: ')

    def run(self):
        action = input('Выберите действие: 1 запись, 2 чтение\n')

        if action == '1':
            phone, name, email = self.get()
            status, result = Controller().post(phone=phone, name=name, email=email)
            if status == 200:
                print('Абонент сохранен', status)
                print(result)
            elif status == 400:
                print('Абонент существует', status)
                print(result)
            elif status == 404:
                print(
                    'Номер абонента должен быть ввида: +79998887766 или 89998887766\n' 'Имя может содежать только буквы\n' 'Почта абонента должен быть ввида: a1@ya.ru')
                self.run()

        elif action == '2':
            phone = self.filter()
            status, result = Controller().get(phone=phone)
            if status == 200:
                print('Абонент найден', status)
                print(result)
            elif status == 400:
                print('Абонента не существует', status)
                action_to_save = input('Сохранить абонента? да/нет')
                if action_to_save == 'да':
                    phone, name, email = self.get()
                    status, result = Controller().post(phone=phone, name=name, email=email)
                    if status == 200:
                        print('Абонент сохранен', status)
                else:
                    self.run()
            elif status == 404:
                print('Номер абонента должен быть ввида: +79998887766 или 89998887766')
                self.run()


def main():
    Interface().run()


if __name__ == "__main__":
    main()
