# %%
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {"author": author, "status": "Available"}

    def borrow_book(self, title):
        if title not in self.books:
            return "Book does not exist"
        if self.books[title]["status"] == "Borrowed":
            return "Book already borrowed"

        self.books[title]["status"] = "Borrowed"
        return f"You borrowed '{title}'"

    def return_book(self, title):
        if title not in self.books:
            return "Book does not exist"

        self.books[title]["status"] = "Available"
        return f"You returned '{title}'"

    def show_books(self):
        result = "\nLibrary Books:\n"
        for title, info in self.books.items():
            result += f"{title} | Author: {info['author']} | Status: {info['status']}\n"
        return result


library = Library()

# 📌 Adding books (title + author)
library.add_book("Python Programming", "Guido van Rossum")
library.add_book("Data Structures", "Mark Weiss")
library.add_book("OOP Concepts", "Bjarne Stroustrup")

print(library.borrow_book("Python Programming"))
print(library.return_book("Python Programming"))
print(library.show_books())

class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        if self.hours_worked > 160:
            overtime_hours = self.hours_worked - 160
            base_salary = 160 * self.hourly_rate
            overtime_pay = overtime_hours * self.hourly_rate * 1.5
        else:
            base_salary = self.hours_worked * self.hourly_rate
            overtime_pay = 0

        total = base_salary + overtime_pay

        return f"""
Employee Name: {self.name}
Hourly Rate: {self.hourly_rate}
Hours Worked: {self.hours_worked}
Base Salary: {base_salary}
Overtime Pay: {overtime_pay}
Total Salary: {total}
"""


# 📌 Employee data
emp1 = Employee("Roxanne", 100, 170)
emp2 = Employee("John Cruz", 120, 150)
emp3 = Employee("Maria Santos", 90, 180)

print(emp1.calculate_salary())
print(emp2.calculate_salary())
print(emp3.calculate_salary())# %%

# %%
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Cart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, product, quantity):
        if quantity > product.stock:
            return f"Not enough stock for {product.name}"

        product.stock -= quantity

        if product.name in self.items:
            self.items[product.name]["qty"] += quantity
        else:
            self.items[product.name] = {
                "price": product.price,
                "qty": quantity
            }

        self.total += product.price * quantity
        return f"Added {quantity} {product.name}(s)"

    def remove_item(self, product):
        if product.name not in self.items:
            return "Item not found in cart"

        qty = self.items[product.name]["qty"]
        self.total -= self.items[product.name]["price"] * qty
        product.stock += qty
        del self.items[product.name]

        return f"Removed {product.name}"

    def show_cart(self):
        result = "\nCart Summary:\n"
        for name, info in self.items.items():
            result += f"{name} | Qty: {info['qty']} | Total: {info['price'] * info['qty']}\n"
        result += f"Grand Total: {self.total}"
        return result


# 📌 Products (name, price, stock)
p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 10)
p3 = Product("Keyboard", 1500, 7)

cart = Cart()

print(cart.add_item(p1, 1))
print(cart.add_item(p2, 2))
print(cart.add_item(p3, 1))
print(cart.remove_item(p2))
print(cart.show_cart())

# %%
