# Initial dictionary of books
books = {
    ("1984", "George Orwell"): "Dystopian",
    ("To Kill a Mockingbird", "Harper Lee"): "Classic",
    ("The Great Gatsby", "F. Scott Fitzgerald"): "Classic"
}

# Add a new book named "Brave New World"
books[("Brave New World", "Aldous Huxley")] = "Dystopian"

# Retrieve and print the genre of "1984"
book_info = books[("1984", "George Orwell")]
print("1984's genre:", book_info)

# Retrieve and print the genre of "Brave New World"
book_info = books[("Brave New World", "Aldous Huxley")]
print("Brave New World's genre:", book_info)
