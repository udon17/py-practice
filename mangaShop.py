class Manga:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class BookStore:
    def __init__(self):
        self.mangas = []
        self.cart = {}

    def add_manga(self, title, price):
        manga = Manga(title, price)
        self.mangas.append(manga)

    def add_to_cart(self, title, quantity):
        for manga in self.mangas:
            if manga.title == title:
                self.cart[title] = self.cart.get(title, 0) + quantity
                print(f"{quantity} copies of {title} were added to your cart.")
                return
        print(f"We couldn't find {title} in the store.")

    def calculate_total(self):
        total = sum([manga.price * self.cart[manga.title] for manga in self.mangas if manga.title in self.cart])
        return total

    def checkout(self):
        total = self.calculate_total()
        print(f"Your total is: {total} yen")
        self.cart = {}  # reset the cart after checkout


# Initialize the bookstore
bookstore = BookStore()

# Add manga to the bookstore
bookstore.add_manga("〇ンピース", 400)
bookstore.add_manga("〇〇の奇妙な冒険", 420)
bookstore.add_manga("〇〇の巨人", 500)

# Take user input for manga title and quantity
title = input("Which manga would you like to buy? ")
quantity = int(input("How many copies would you like to buy? "))

# Add manga to cart
bookstore.add_to_cart(title, quantity)

# Checkout
bookstore.checkout()
