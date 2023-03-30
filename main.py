from store import Store
from shop import Shop
from request import Request

store = Store()
shop = Shop()

store_items = {"апельсины": 30,
               "яблоки": 40,
               "огурцы": 10,
               "помидоры": 10}

storages = {"склад": store, "магазин": shop}

for storage in storages.values():
    for product, qnt in store_items.items():
        if storage == shop:
            qnt //= 10
            storage.add(product, qnt)
        else:
            storage.add(product, qnt)


def main():
    print("Здравствуйте!")

    while True:
        for place_r, place in storages.items():
            print(f"\nВ {place_r} хранится:\n")
            [print(f"{qnt} {item}") for item, qnt in place.get_items().items()]

        print("\nПожалуйста, введите строку формата 'Доставить 3 печеньки из склад в магазин'")
        print("Или введите ' stop', чтобы завершить")
        user_input = input('')

        if user_input.lower() == "stop":
            break

        request = Request(storages, user_input)
        storages[request.departure].remove(request.product, request.amount)
        print(f"Курьер забирает {request.amount} {request.product} из {request.departure}")
        print(f"Курьер везет {request.amount} {request.product} со {request.departure} в {request.destination}")
        storages[request.destination].add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} в {request.destination}")


if __name__ == "__main__":
    main()
