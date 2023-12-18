class book:
    def __init__(self, name, author, date, publisher):
        self.book_name=name
        self.book_author=author
        self.book_date=date
        self.book_publisher=publisher
    
    def add_book(self):
        print("Name: " + self.book_name)
        print("Author: "+self.book_author)
        print("Date Published: "+self.book_date)
        print("Book Publisher: " +self.book_publisher)
        print("Book Added")

book1=book("Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", "July 8, 1999", "Bloomsbury and Scholastic, Inc")
book1.add_book()

book2=book("Lord of the Rings", "J. R. R. Tolkien", "July 29, 1954", "N/A")
book2.add_book()