from abc import ABC, abstractmethod


class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, item: str, quantity: int):

        if quantity > self._get_free_space():
            not_distributed_count = quantity - self._get_free_space()

            if self.items.get(item) is None:
                self.items[item] = self._get_free_space()
            else:
                self.items[item] += self._get_free_space()
            print(f'Достигнута максимальная ёмкость. {not_distributed_count} шт. '
                  f'товара не удалось распределить')

        else:
            # Обработка случая, когда в словаре ещё нет такого товара. Иначе возникнет keyerror
            if self.items.get(item) is None:
                self.items[item] = quantity
            else:
                self.items[item] += quantity
            print(f'Успешно добавлено {quantity} шт. {item}')

    @abstractmethod
    def remove(self, item: str, quantity: int):
        '''
        Функция возвращает количество товара, которое было убрано со склада
        '''
        if self.items.get(item) is None:
            print('Такого товара нет')
            return 0

        current_quantity = self.items[item]

        if current_quantity < quantity:
            self.items[item] = 0
            print(f'Количество товаров {item} достигло 0. {quantity - current_quantity} товаров'
                  f'не удалось убрать')

            return current_quantity

        else:
            self.items[item] -= quantity
            print(f'Убрано {quantity} шт. товара {item}. Осталось {self.items[item]} шт.')
            return quantity

    def get_items(self):
        total_items = ""
        for item, quantity in self.items.items():
            total_items += f'{item} - {quantity} шт.\n'

        return total_items

    def _get_free_space(self):
        current_utilization = sum(self.items.values())
        return self.capacity - current_utilization

    def _get_unique_items_count(self):
        return len(self.items)
