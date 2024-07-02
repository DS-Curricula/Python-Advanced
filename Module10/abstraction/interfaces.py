from abc import ABC, abstractmethod


# Abstract class 'Printable' acts as an interface
class Printable(ABC):
    # Abstract method that must be implemented by any subclass
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Implement the abstract 'print_info' method
    def print_info(self):
        print(f"Book: {self.title}  by {self.author}")


# Create an instance of the 'Book' class and call the 'print_info' method
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book.print_info()  # Output: Book: The Great Gatsby by F. Scott Fitzgerald
