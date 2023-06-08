class Person:
    id_counter = 100

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.user_id = Person.generate_id()

    @classmethod
    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id

    def __repr__(self) -> str:
        return f"email: {self.email} seller_id: {self.user_id}"


class Store:
    def __init__(self) -> None:
        self.total_product = {}

    def add_product(self, seller_id, product):
        product_dict = vars(product)
        if seller_id not in self.total_product:
            self.total_product[seller_id] = []
            # add sell info
            seller_info = {}
            seller_info["total_sell_product"] = 0
            seller_info["total_sell_amount"] = 0
            seller_info["total_profit_amount"] = 0
            self.total_product[seller_id].append(seller_info)
        self.total_product[seller_id].append(product_dict)


class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"product name:{self.name}, price:{self.price} quantity:{self.quantity}"


class Owner(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)


class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    # sell info individual user
    def sell_info(self, store):
        print("seller id :",self.user_id,"s' sell info:")
        print("--------------")
        print("total product sell:",store.total_product[self.user_id][0]['total_sell_product'],"pices")
        print("total sell amount:",store.total_product[self.user_id][0]['total_sell_amount'],"usd.")
        print("total profit amount:",store.total_product[self.user_id][0]['total_profit_amount'],"usd.")

      # add product
    def add_product(self, store, product_name, product_price, product_quantity):

        product = Product(product_name, product_price, product_quantity)
        store.add_product(self.user_id, product)
        # print(product)


class Customer(Person):
    def __init__(self, email, password) -> None:
        self.total_buy_amount = 0
        self.total_buy_product = 0
        super().__init__(email, password)

    def buy_product(self, store, seller_id, product_name, quantity):
        for index in range(1, len(store.total_product[seller_id])):
            product = store.total_product[seller_id][index]
            if product["name"] != product_name:
                return (f"{product_name} not match")

            elif product["name"] == product_name and product["quantity"] < quantity:
                return ("seller has only", {product["quantity"]}, "product")

            else:
                self.total_buy_product += quantity
                product["quantity"] -= quantity
                self.total_buy_amount += quantity * product["price"]
                
                #update seller sell info....
                seller = store.total_product[seller_id][0]

                seller["total_sell_product"] += quantity
                seller["total_sell_amount"] += quantity * product["price"]
                seller["total_profit_amount"] += quantity * product["price"] * 0.1
                return f"buy successfully!"

    def show_products(self, store):
        all_seller_keys = store.total_product.keys()
        for seller_id in all_seller_keys:
            print("seller_id:", seller_id)
            print("--------------")
            for index in range(1, len(store.total_product[seller_id])):
                product = store.total_product[seller_id][index]
                print("name:", product["name"], "price:",
                      product["price"], "quantity:", product["quantity"])
            print()


store = Store()
seller1 = Seller('seller1@email.com', 1234)
seller2 = Seller('seller2@email.com', 1235)
seller3 = Seller('seller3@email.com', 1234)

# print(seller1)
# print(seller2)
# print(seller3)
seller1.add_product(store, 'Iphone10', 150, 15)
seller1.add_product(store, 'Iphone11', 200, 10)

seller2.add_product(store, 'samsung14', 150, 12)
seller2.add_product(store, 'samsung12', 170, 11)

seller3.add_product(store, 'oppo-f9', 150, 12)
seller3.add_product(store, 'oppo-nord6', 120, 11)


customer1 = Customer('customer1@gmail.com', 1234)
# customer1.show_products(store)
customer1.buy_product(store, 100, 'Iphone10', 5)

# print(store.total_product)
# x = customer1.buy_product(store, 100, 'Iphone10', 5)
# print(x)
# print()
# customer1.show_products(store)
seller1.sell_info(store)
print()
seller2.sell_info(store)
print()
customer1.buy_product(store, 101, 'samsung12', 5)
seller2.sell_info(store)
