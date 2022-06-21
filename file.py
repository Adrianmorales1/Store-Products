class Product:
    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increase):
        if is_increase:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price / (1 - percent_change)
    
    def print_info(self):
        print(f'Name of Product: {self.name}')
        print(f'Category of Product: {self.category}')
        print(f'Price of Product: {self.price}')

class Store:
    def __init__(self, name) -> None:
        self.name = name
        self.list = []
    def add_product(self, new_product:Product):
        self.list.append(new_product)
    def sell_product(self, id):
        self.list[id].print_info()
        self.list.pop(id)
    def inflation(self, percent_increase):
        for x in self.list:
            num = x.price * (1 + percent_increase)
            x.price = round(num, 2)
    def set_clearance(self, category, percent_discount):
        for x in self.list:
            if x.category == category:
                num = x.price * (1 + percent_discount)
                x.price = round(num, 2)
                print(x.price)
        print(f'Clearance Items: {category}')




grass = Product('Green Grass', 49.99, "Nature")
water_bottle = Product('Water Bottle', 19.99, "Bottle")
cool_bottle = Product('Cool Bottle', 14.99, "Bottle")
nice_bottle = Product('Nice Nice Bottle', 24.99, "Bottle")
grass.print_info()
forest_plus = Store('Forest Plus')
forest_plus.add_product(nice_bottle)
forest_plus.add_product(grass)
forest_plus.add_product(cool_bottle)
forest_plus.add_product(water_bottle)
forest_plus.inflation(0.01)
forest_plus.set_clearance('Bottle', .10)
#forest_plus.sell_product(0)