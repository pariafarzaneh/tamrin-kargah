# تعریف کلاس Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("عنوان:", self.title)
        print("نویسنده:", self.author)
        print("قیمت:", self.price)

    def apply_discount(self, discount):
        if 0 <= discount <= 1:
            self.price = self.price * (1 - discount)
        else:
            print("درصد تخفیف باید بین 0 تا 1 باشد.")

# ایجاد شی از کلاس Book
book1 = Book("شازده کوچولو", "آنتوان دوسنت اگزوپری", 120000)

# نمایش اطلاعات اولیه
print("اطلاعات اولیه کتاب:")
book1.display_details()

# اعمال