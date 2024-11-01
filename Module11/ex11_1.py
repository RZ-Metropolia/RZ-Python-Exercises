class Publication():
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book", end= " ")
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine", end=" ")
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")


# main program
magazine_0 = Magazine("Donald Duck", "Aki Hyyppä")
magazine_0.print_information()

print("\n")

book_0 = Book("Compartment No. 6", "Rosa Liksom", "192")
book_0.print_information()