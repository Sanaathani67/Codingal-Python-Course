class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        self.is_borrowed=True
        print(self.title,"book has been borrowed!")
        
    def return_book(self):
        self.is_borrowed=False
        print(self.title,"book has been returned!")

    def __str__(self):
        return f"the title is {self.title}, and the author is {self.author}"

book_1= Book("Tom Gates", "Liz Pichon")
book_2=Book("Wonder", " R.J Palacio")
book_3=Book("War horse", "Michael Morpurgo")

print(book_1)
print(book_2)
print(book_3)

book_1.borrow()
book_1.return_book()

book_2.borrow()
book_2.return_book()

book_3.borrow()
book_3.return_book()