from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from models import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')
        self.__order = []
        self.__price = 0

    def __set_slots(self):
        self.__win.order_amerikan.clicked.connect(self.order_amerikan_pizza)
        self.__win.order_italian.clicked.connect(self.order_italian_pizza)
        self.__win.order_moms.clicked.connect(self.order_moms_pizza)
        self.__win.check_order.clicked.connect(self.check_ordered_pizza)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def order_amerikan_pizza(self):
        self.extra_ingredient_checker(American())

    def order_italian_pizza(self):
        self.extra_ingredient_checker(Italian())

    def order_moms_pizza(self):
        self.extra_ingredient_checker(Moms())

    def extra_ingredient_checker(self, pizza: Pizza):
        if self.__win.extra_sausege.checkState():
            pizza = ExtraIngredients(pizza, "Колбаса", 5)
        if self.__win.extra_chese.checkState():
            pizza = ExtraIngredients(pizza, "Сыр", 5)
        if self.__win.extra_seafood.checkState():
            pizza = ExtraIngredients(pizza, "Морепродукты", 5)
        if self.__win.extra_souse.checkState():
            pizza = ExtraIngredients(pizza, "Соус", 5)
        if self.__win.extra_pepper.checkState():
            pizza = ExtraIngredients(pizza, "Перец", 5)
        self.__order.append(pizza.__str__())
        self.__price += pizza.get_price

    def check_ordered_pizza(self):
        QMessageBox.information(self, 'Ваш заказ:', f'{self.__order}, к оплате: {self.__price}')
        self.__order = []
        self.__price = 0
