class Human:
    default_name = ''
    default_age = ''

    def __init__(self,money, house=None, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        return f'{self.name} {self.age} {self.__money} {self.__house}'

    @staticmethod
    def default_info():
        default_name = 'Jack'
        default_age = 33
        return f'{default_name} {default_age}'

    def make_deal(self, house, price):
        self.__money-=price
        self.__house = house

    def earn_money(self, value):
        if isinstance(value, int):
            self.__money+=value
            return self.__money
        else:
            return f'Значение долно быть числом'

    def buy_house(self, house, price):
        if self.__money>price:
            self.__money-=price
            self.__house = house
            return f'Вы можите совершить сделку. Остаток на счету {self.__money}'
        else:
            return f'Недостаточно средств'


class House:

    def  __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        self.sale = sale
        self._price-=self.sale
        return self._price


class SmallHouse(House):

    def __init__(self, price, area=40):
        super().__init__(price, area)






d = Human(money=400)
d = Human(money=400, name='Mike', age=29)
print(d.info())
h = SmallHouse(price=500)
print(d.buy_house(price=h._price, house=h._area))
print(d.earn_money(300))
print(d.buy_house(price=h._price, house=h._area))
print(d.__dict__)
