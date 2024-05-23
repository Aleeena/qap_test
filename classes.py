class Figure:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.height}"


rect = Figure(5, 10, 50, 100)


class Client:
    def __init__(self, f_name, l_name, town, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.town = town
        self.balance = balance

    def __str__(self):
        return f"{self.f_name} {self.l_name}. {self.town}. Баланс: {self.balance} руб."


print(rect)

customer = Client("Иван", "Петров", "Москва", 50)
print(customer)
