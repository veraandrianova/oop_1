#Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).
#В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычная газировка».

class Soda:

    def __init__(self, value):
        if isinstance(value, str):
            self.value = value

        else:
            self.value = None

    def show_my_drink(self):
        if self.value:
            return f'Газировка с {self.value}'
        else:
            return f'Обычная газировка'

d = Soda(5)
f = Soda('малина')
print(d.show_my_drink())
print(f.show_my_drink())


#Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
#Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
#С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# ;
#– С отрицательными числами ничего не выйдет!;
#– Нужно вводить только числа!;
#– Жаль, но из этого треугольник не сделать.
#
class TriangleChecker:

    def __init__(self, a,b,c):
        self.border1 = a
        self.border2 = b
        self.border3 = c

    def is_triangle(self):
        if (not isinstance(self.border1, int)) or (not isinstance(self.border2, int)) or (not isinstance(self.border3, int)):
            return f'Нужно вводить только числа!'
        if self.border1<0 or self.border2<0 or self.border3<0:
            return f'С отрицательными числами ничего не выйдет!'

        else:
            if (isinstance(self.border1, int)) or (isinstance(self.border2, int)) or (isinstance(self.border3, int)):
                if self.border1>0 or self.border2>0 or self.border3>0:
                    if self.border1 + self.border2 > self.border3:
                        return f'Ура, можно построить треугольник!'
                    return f'Жаль, но из этого треугольник не сделать.'


d = TriangleChecker(1,2,4)
print(d.is_triangle())
#Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она реализовала
# методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг.
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов.

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.2

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        if isinstance(value, (int, float)):
            self.__kg = value
        return f'Должны быть числа'

d = KgToPounds(2)
d.kg = 3
print(d.to_pounds())

#Николай – оригинальный человек.
#Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
#Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
#В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, например,
# Максим, то оно преобразуется в “Я не Максим, а Николай”.
#Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и
# вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод
# «приветствие», то ничего у такого хитреца не получится).

class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.name != 'Николай':
            self.name = f'Николай'


d = Nikola('Николай', 29)
print(d.name)
