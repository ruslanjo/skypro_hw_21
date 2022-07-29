from store_and_shop import Shop, Store
from request import Request


store_products = {"печеньки": 10,
                  "вафли": 10,
                  "пряники": 10,
                  "конфеты": 10,
                  "игрушки": 10,
                  "машинки": 5,
                  "питоны": 5,
                  "инкапсуляции": 5}

store = Store(store_products)
shop = Shop()

if __name__ == "__main__":
    print('Добро пожаловать в нашу логистическую компанию.')

    user_input = input('Введите ваш запрос. Чтобы завершить работу введите "стоп": ').lower()

    while user_input != "стоп":
        request = Request(user_input)

        item = request.product
        quantity = request.amount

        removed_from_store = store.remove(item, quantity)
        if removed_from_store > 0:
            shop.add(item, removed_from_store)
        else:
            print('Товар не доставлен в магазин, т.к. закончился на складе')


        print('\n############СТАТУС################')
        print('На складе хранится:')
        print(store.get_items())

        print('В магазине хранится:')
        print(shop.get_items())

        user_input = input('Введите ваш запрос. Чтобы завершить работу введите "стоп": ').lower()
