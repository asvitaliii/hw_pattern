class Pizza:
    def __init__(self, name: str, price: float, ingredients: list, extra_ingredients: list):
        self._name = name
        self._price = price
        self._ingredients = ingredients
        self._extra_ingredients = extra_ingredients

    def __str__(self):
        return self.get_name

    @property
    def get_name(self):
        return self._name

    @property
    def get_price(self):
        return self._price

    @property
    def get_ingredients(self):
        return self._ingredients

    @property
    def get_extra_ingredients(self):
        return self._extra_ingredients


class ExtraIngredients(Pizza):
    def __init__(self, pizza: Pizza, extra_ingredient_name: str, extra_ingredient_price: float):
        super().__init__(pizza.get_name, pizza.get_price + extra_ingredient_price, pizza.get_ingredients, pizza.get_extra_ingredients)
        self._extra_ingredients.append(extra_ingredient_name)

    def __str__(self):
        return f"{self._name} с дополнительными ингредиентами: {[i for i in self._extra_ingredients]}"


class American(Pizza):
    def __init__(self):
        super().__init__("Американская", 150, ["колбаса", "сыр", "соус", "грибы"], [])


class Italian(Pizza):
    def __init__(self):
        super().__init__("Итальянская", 160, ["морепродукты", "оливки", "соус"], [])


class Moms(Pizza):
    def __init__(self):
        super().__init__("Мамина", 200, ["Всё, что есть в холодильнике...)"], [])
