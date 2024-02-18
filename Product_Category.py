from enum import Enum


class ProductCategory(Enum):
    ELECTRONICS = 1
    GROCERIES = 2
    UTENSILS = 3
    CLOTHING = 4


class CardType(Enum):
    MASTER_CARD = 1
    VISA_CARD = 2
    VERVE = 3
    AMERICAN_EXPRESS = 4


class User:
    def _init_(self, age, email, home_address, name, password, phone):
        self.age = age
        self.email = email
        self.home_address = home_address
        self.name = name
        self.password = password
        self.phone = phone


class Customer(User):
    def _init_(self, age, email, home_address, name, password, phone):
        super()._init_(age, email, home_address, name, password, phone)
        self.billing_information_list = []
        self.shopping_cart = ShoppingCart()


class Seller(User):
    pass


class Admin(User):
    pass


class Product:
    def _init_(self, product_id, product_name, price, product_description, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_description = product_description
        self.category = category


class BillingInformation:
    def _init_(self, receiver_phone, receiver_name, delivery_address, credit_card_information):
        self.receiver_phone = receiver_phone
        self.receiver_name = receiver_name
        self.delivery_address = delivery_address
        self.credit_card_information = credit_card_information


class CreditCardInformation:
    def _init_(self, card_cvv, expiration_year, expiration_month, credit_card_number, name_on_card, card_type):
        self.card_cvv = card_cvv
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.credit_card_number = credit_card_number
        self.name_on_card = name_on_card
        self.card_type = card_type


class Address:
    def _init_(self, city_name, country_name, house_number, street, state):
        self.city_name = city_name
        self.country_name = country_name
        self.house_number = house_number
        self.street = street
        self.state = state


class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class CartItem:
    def _init_(self, quantity, product):
        self.quantity = quantity
        self.product = product
