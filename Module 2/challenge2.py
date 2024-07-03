# Initial dictionary of books
books = {
    "1984": ("George Orwell", "Dystopian"),
    "To Kill a Mockingbird": ("Harper Lee", "Classic"),
    "The Great Gatsby": ("F. Scott Fitzgerald", "Classic")
}

# Add a new book named "Brave New World"
books["Brave New World"] = ("Aldous Huxley", "Dystopian")

# Retrieve and print the author and genre of "1984"
book_info = books["1984"]
print("1984's author:", book_info[0])
print("1984's genre:", book_info[1])

# Retrieve and print the author and genre of "Brave New World"
book_info = books["Brave New World"]
print("Brave New World's author:", book_info[0])
print("Brave New World's genre:", book_info[1])
