from storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        self._items = items
        self._capacity = capacity

    ######## Геттеры и сеттеры #########

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, val: dict):
        self._items = val

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, val: int):
        self._capacity = val

    #################################

    def add(self, item: str, quantity: int):
        print('========Добавляем товар на склад========')
        super().add(item, quantity)

    def remove(self, item: str, quantity: int):
        print('========Удаляем товар со склада========')
        return super().remove(item, quantity)


class Shop(Storage):
    def __init__(self, items: dict = None, capacity: int = 20):

        if items is None:
            items = {}

        else:
            if len(items) > 5:
                print('Не удалось инициализировать магазин. Количество уникальных товаров д.б. <= 5\n')
                return

        self._items = items
        self._capacity = capacity

    ########## Геттеры и Сеттеры ##############

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, val):
        if len(val) > 5:
            print('Не удалось изменить магазин. Количество уникальных товаров д.б. <= 5')
            return
        self._items = val

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, val):
        self._capacity = val

    ##################################

    def add(self, item: str, quantity: int):
        print('========Добавляем товар в магазин========')

        # Если уже 5 товаров, то при добавлении ещё одного будет переполнение. Иначе добавить товар можно
        if self._get_unique_items_count() > 5:
            print('Не получилось добавить товары. В магазине может быть только 5 уникальных товаров')
            return

        super().add(item, quantity)

    def remove(self, item: str, quantity: int):
        print('========Удаляем товар из магазина========')

        super().remove(item, quantity)
