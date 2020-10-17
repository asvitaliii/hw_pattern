from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def __str__(self):
        return f'{self.get_name()} пицца за {self.get_price()}'

    @abstractmethod
    def get_name(self):
        return self._name

    @abstractmethod
    def get_price(self):
        return self._price


class American(Pizza):
    def __init__(self):
        super().__init__("Американская", 150)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


class Italian(Pizza):
    def __init__(self):
        super().__init__("Итальянская", 160)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


class Moms(Pizza):
    def __init__(self):
        super().__init__("Мамина", 200)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


class ExtraCheese(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_name(), pizza.get_price())
        self._pizza = pizza

    def get_name(self):
        return self._name

    def get_price(self):
        return self._pizza.get_price() + 10


class ExtraSausage(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_name(), pizza.get_price())
        self._pizza = pizza

    def get_name(self):
        return self._name

    def get_price(self):
        return self._pizza.get_price() + 10


class ExtraSeafood(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_name(), pizza.get_price())
        self._pizza = pizza

    def get_name(self):
        return self._name

    def get_price(self):
        return self._pizza.get_price() + 15


class ExtraPepper(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_name(), pizza.get_price())
        self._pizza = pizza

    def get_name(self):
        return self._name

    def get_price(self):
        return self._pizza.get_price() + 10


class ExtraSouse(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_name(), pizza.get_price())
        self._pizza = pizza

    def get_name(self):
        return self._name

    def get_price(self):
        return self._pizza.get_price() + 5
