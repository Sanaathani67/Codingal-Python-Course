books = ["Python Basics", "Data Structures", "Web Development", "AI Programming"]
copies = [3, 2, 0, 4]

library = {book: copy for book, copy in zip(books, copies)}

print("Library:", library)

available_books = [book for book in books if library[book] > 0]

print("Available books:", available_books)

chosen_book = input("Which book do you want to borrow? ")

if chosen_book not in library or library[chosen_book] == 0:
    print("Sorry, that book is unavailable.")
    exit()

late_fees = [2, 3, 1, 4]

extra_fee = float(input("Enter an extra late fee: "))

late_fees = list(map(lambda fee: fee + extra_fee, late_fees))

print("Updated late fees:", late_fees)

book_index = books.index(chosen_book)

print("Chosen book index:", book_index)
print("Updated fee:", late_fees[book_index])

library[chosen_book] -= 1

print("Final Library Summary:")
print(library)