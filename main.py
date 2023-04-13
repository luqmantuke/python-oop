class Book:
    def __init__(self, title,quantity,author,price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None


    def set_discount(self,discount):
        self.__discount = discount

    
    def get_price(self):
        if self.__discount:
            return self.__price * self.quantity * (1-self.__discount)
        
        return self.__price * self.quantity
        

    def __repr__(self):
       return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
    

class Novel(Book):
    def __init__(self, title, quantity, author, price,pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages
    def __repr__(self):
        return f"Novel: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Academic(Book):
    def __init__(self, title, quantity, author, price,branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
    def __repr__(self):
       return f"Academic: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


novel1 = Novel('Two States', 1, 'Chetan Bhagat', 200, 100)
novel1.set_discount = 0.5

academic1 = Academic('Two States', 1, 'Chetan Bhagat', 200, 'Ilala')



print(novel1)
print(academic1)
