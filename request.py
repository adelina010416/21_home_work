class Request:
    def __init__(self, places, request):
        data = request.lower().split(" ")
        try:
            self._departure = data[-3]
            self._destination = data[-1]
            self._product = data[2]
        except IndexError:
            raise Exception("InvalidRequest")
        try:
            self._amount = int(data[1])
        except TypeError:
            raise Exception("Invalid Type for Amount")

        if self._departure not in places.keys() or self._destination not in places.keys():
            raise Exception("InvalidStoreName")

        if len(data) != 7:
            raise Exception("InvalidRequest")

    @property
    def destination(self):
        return self._destination

    @property
    def departure(self):
        return self._departure

    @property
    def product(self):
        return self._product

    @property
    def amount(self):
        return self._amount
