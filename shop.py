from store import Store


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._items = {}          # {title: qnt}
        self._capacity = 20

    def add(self, title, qnt):
        """Увеличивает запас items с учетом лимита capacity"""
        self.check_qnt(qnt)
        if self.capacity == 0:
            raise Exception(f"We cannot add {title}: there is no empty space in Shop.")

        if title in self.items.keys():
            if qnt < self.capacity:
                self.items[title] = qnt + self.items.get(title)
            else:
                self.items[title] = self.capacity + self.items.get(title)

        else:
            if len(self.items) >= 5:
                raise Exception("fWe cannot add {title}: there is no empty space in Shop.")
            else:
                if qnt < self.capacity:
                    self.items[title] = qnt
                else:
                    self.items[title] = self.capacity
        self.get_free_space("add", qnt)
