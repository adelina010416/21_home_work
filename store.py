from storage_abstract import Storage


class Store(Storage):
    def __init__(self):
        self._items = {}          # {title: qnt}
        self._capacity = 100

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_qnt):
        if new_qnt >= 0:
            self._capacity = new_qnt
        else:
            self._capacity = 0

    def add(self, title, qnt):
        """Увеличивает запас items с учетом лимита capacity"""
        self.check_qnt(qnt)
        if self.capacity == 0:
            raise Exception(f"We cannot add {title}: there is no empty space in Store.")

        elif qnt < self.capacity and title in self.items.keys():
            self.items[title] = qnt + self.items.get(title)

        elif qnt < self.capacity and title not in self.items.keys():
            self.items[title] = qnt

        elif qnt >= self.capacity and title in self.items.keys():
            self.items[title] = self.capacity + self.items.get(title)

        else:
            self.items[title] = self.capacity
        self.get_free_space("add", qnt)

    def remove(self, title, qnt):
        """Уменьшает запас items, но не ниже 0"""
        self.check_qnt(qnt)
        amount = self.items.get(title, None)
        if amount is not None:
            if qnt >= self.items.get(title):
                self.items[title] = 0
                del self._items[title]
            else:
                self.items[title] -= qnt
        else:
            raise Exception(f"There is no {title} in Store")
        self.get_free_space("remove", qnt)

    def get_free_space(self, flag, qnt):
        """Возвращает количество свободных мест (capacity)"""
        if flag == "add":
            self.capacity = self.capacity - qnt
        else:
            self.capacity = self.capacity + qnt

    def get_items(self):
        """Возвращает содержание склада в словаре {товар: количество} (items)"""
        return self.items

    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров (items.keys)"""
        return len(self.items.keys())

    def check_qnt(self, qnt):
        """Проверяет введённое число"""
        if qnt <= 0:
            raise ValueError("Please, use only positive numbers greater than 0")
        try:
            int(qnt)
        except ValueError:
            print(type(qnt))
            raise TypeError("Please, use only numbers")
