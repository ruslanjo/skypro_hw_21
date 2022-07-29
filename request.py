class Request:
    def __init__(self, init_string):
        '''
        При инициализации  принимает строку типа

        Доставить 3 печеньки из склад в магазин

        И возвращает объект класса Request
        '''
        self._from = init_string.split()[-3]
        self._to = init_string.split()[-1]
        self._amount = int(init_string.split()[1])
        self._product = init_string.split()[2]

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
