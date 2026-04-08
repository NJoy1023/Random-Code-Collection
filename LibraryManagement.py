#Book Class represents each book object's attributes and behavior
class Book:

    # Initializes a book object with attributes
    def __init__(self,title,author_name, year_of_birth, genre, is_available):
        self.title = title
        self.author_name = author_name
        self.year_of_birth = year_of_birth
        self.genre = genre
        self.is_available = is_available
        self.author = (self.author_name,self.year_of_birth)  #Author information compressed into tuple

    #Borrowing marks book as unavailable 
    def borrow_book(self):
        self.is_available = False
        print(f"{self.title} has been borrowed")

    #Returning marks book as available 
    def return_book(self):
        self.is_available = True
        print(f"{self.title} has been returned")

#Library Class manages book storage and methods to access them
class Library:

    #Initialize the collection of book
    def __init__(self):
        self.books = [] # List of book objects
        self.genres = set() # Set of genres, no duplicates
        self.authors_books = {} #Dictionary of authors and their list of books

    #Adds book to the Library
    def add_book(self,book):

        self.books.append(book) #Adds book object in Library list
        self.genres.add(book.genre) #Adds genre in Library set
        if book.author_name not in self.authors_books: #Adds authors-books in Library dictionary
            self.authors_books[book.author_name] = []
        self.authors_books[book.author_name].append(book.title)

        print(f"{book.title} added to Library")
    
    #Removes book from Library collections by title
    def remove_book(self, book):

        for j in self.books:
            if j.title == book:
                self.books.remove(j) #Removes book object from Library List
                self.genres.remove(j.genre) #Removes book genre from Library set
                self.genres.add(j.genre) #Checks if any stored book shares the same genre, re-store if found
        print(f"{j.title} removed from Library")

        for key, value in self.authors_books.items(): #Removes book from author-books Library dictionary
            for v in value:
                if v == book:
                    value.remove(v)

    #Shows all the books of a specific author
    def find_books_by_author(self, author_name):
        for author, aBooks in self.authors_books.items():
            if author == author_name:
                organizeABooks = ' \n- '.join(aBooks)
                print(f"Books of {author_name} : \n- {organizeABooks}")
                return True
        print(f"Books of {author_name}: \nNo books found...")
    
    #Shows all books under a specific genre
    def find_books_by_genre(self, genre):
        print(f"Books under {genre} genre :")
        for b in self.books:
            if b.genre == genre:
                print(" -", b.title)
        if genre not in self.genres:
            print(f"No books found...")
    
    #Shows all books and their availability status
    def show_all_books(self):
        for b in self.books: #Sets the availability status
            if b.is_available == True:
                self.status = "Available"
            else:
                self.status = "Borrowed"

            print(f"{b.title} by {b.author_name} ({self.status})")

#User Class represents a Library user
class User:
    #Initializes user w/ name and their borrowed books
    def __init__(self, name):
        self.name = name
        self.borrowed_books = set()

    #User borrows a book, updating book's status in user and library's records
    def borrow_book(self, library, book_title):
        for b in library:
            if book_title == b.title and b.is_available==True:
                self.borrowed_books.add(book_title)
                b.borrow_book()
                return True
        if b.is_available==False:
            print(f"Sorry, {book_title} has already been borrowed by another user")
            return True
        print(f"{book_title} not in Library")
    
    #User returns a book, updating book's status in user and library's records
    def return_book(self, library, book_title):
        for b in library:
            if b.title == book_title:
                b.return_book()
                self.borrowed_books.remove(b.title)
                return True
        print(f"{book_title} not in Library")



#Creating Dog instances w/ book information
b1 = Book("Python Programming","John Doe", 2003,"Programming",True)
b2 = Book("Data Structures","Jane Smith", 2004,"Programming",True)

#Creating Library instance
lib = Library()

#Adds Books objects to the Library Class
lib.add_book(b1)
lib.add_book(b2)

#Creating User instance w/ name
u = User("Nathalie")

#Calls User method to borrow book, changing both the user and library's records
u.borrow_book(lib.books, "Python Programming")

#Calls Library Class method to display all books
lib.show_all_books()





""" Test Runs:
b1 = Book("Python Programming","John Doe", 2003, "Programming",True)
b2 = Book("Data Structures","Jane Smith", 2021, "Programming",True)
b3 = Book("Python Programming ver 2","John Doe",2011,"Programming",True)

u1 = User("Sassy")
u2 = User("Nathalie")


print("===== Add Books ====")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print("===== Remove Books ====")
lib.remove_book("Data Structures")

print("===== Find by Author ====")
lib.find_books_by_author("John Doe")

print("===== Find by Genre ====")
lib.find_books_by_genre("Programming")

print("===== All Books in Library ====")
lib.show_all_books()


print("===== Borrowed Books ====")

u1.borrow_book(lib.books, "Python Programming")
u1.borrow_book(lib.books, "Data Structures")
u1.borrow_book(lib.books, "Python Programming ver 2")
print(f"{u1.name} Borrowed : {' - '.join(u1.borrowed_books)}")

u2.borrow_book(lib.books, "Python Programming ver 2")


print("===== All Books in Library ====")
lib.show_all_books()

print("===== Return Books ====")
u1.return_book(lib.books, "Data Structures")
u1.return_book(lib.books, "Python Programming")
u1.return_book(lib.books, "Python Programming ver 2")
print(f"{u1.name} Borrowed : {' - '.join(u1.borrowed_books)}")

print("===== All Books in Library ====")
lib.show_all_books()

"""