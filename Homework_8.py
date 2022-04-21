# 1*****************************
class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_type(cls, data):
        return f'day {int(data[0]):02d}, momth {int(data[1]):02d}, year {int(data[2])}'

    @staticmethod
    def validation(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'enter invalid date!'

    def data_func(self):
        result_1 = Data.change_type(self.data.split('-'))
        result_2 = Data.validation(self.data.split('-'))
        return result_2 if result_2 else f'reformatted date (тип int)\n{result_1}'


user_data = input('enter date (dd-mm-yy): ')
mc = Data(user_data)
print(mc.data_func())
user_data = input('enter date (dd-mm-yy): ')
mc_2 = Data(user_data)
print(mc_2.data_func())
print(mc.data_func())

# 2*************************

class MyZeDiEr(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            raise MyZeDiEr("Division by zero forbidden!!!")
        return round(s_1 / s_2, 3)
    except ValueError:
        return "Value Error"
    except MyZeDiEr as my:
        return my


print(div(input("Enter first number - "), input("Enter first second - ")))

# 3*******************************

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    inp_data = input("enter number: ")
    if inp_data == "":
        break
    try:
        if inp_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(inp_data))
        else:
            raise OwnError("enter number: ")
    except OwnError as err:
        print(err)
        continue

print(my_list)

# 7**************************

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))


cn = ComplexNumber(1, -2)
cn1 = ComplexNumber(3, 4)
print(cn + cn1)
print(cn * cn1)
print(complex(1, -2) * complex(3, 4))

# 4*********************


class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    ''' Принтер '''

    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Сканер '''


class Copier(OfficeEquipment):
    ''' Копир '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    ''' Склад '''
    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):
        ''' Приём оргтехники на склад '''
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        ''' Выдача оргтехники со склада '''
        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nЗапасы на складе:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')
        print('------------------------------------')

    def issued_equipments(self):
        ''' Вывод информации овыданной оргтехикие '''
        print(f'\nIssued to office:\n{self.__equipments}')


models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet'),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet'),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:

    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:

        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} шт.)'

        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')

            try:
                model = int(input('модель > '))
                if model in range(len(models)):

                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:

                print('\nОперация:')
                if (action == '1'):
                    print(f'Принято на склад {models[model].model} - {n} шт.')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):
                    max = warehouse.num(model)
                    if (n > max):
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    warehouse.issue_Equipment(model, n)

                warehouse.equipments_in_warehouse()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')
