## class methods are callling throungh class

class Book:
    total_books = 0 # class variable

    @classmethod #reffers that the method you will make is relATED TO CLASS
    def increment_book_count(cls): #cls means class pay kaam hai
        cls.total_books +=1 # add plus one when we call this method


if __name__ == "__main__":
    Book.increment_book_count() # we just added one book
    Book.increment_book_count() # we just added second book

    print(f"total books :{Book.total_books}")        