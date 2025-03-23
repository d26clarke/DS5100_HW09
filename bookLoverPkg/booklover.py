import pandas as pd
from typing import Dict

#Create a variable of type dictionary as an empty dictionary with types str and int
book_init: Dict[str, int] = {'book_name':[], 'book_rating':[]}

class BookLover:
    # Class attributes
    num_books: int = 0
    #book_list: pd.DataFrame = pd.DataFrame({'book_name':[], 'book_rating':[]})
    book_list: pd.DataFrame = pd.DataFrame(book_init)
        

    # Instance attributes
    def __init__(self, name: str, email: str, fav_genre: str) -> None:
        assert isinstance(name, str), 'Name must be of type String.' 
        assert isinstance(email, str), 'email must be of type String.' 
        assert isinstance(fav_genre, str), 'fav_genre must be of type String.' 
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    # Instance method add_book
    def add_book(self, book_name: str, rating: int) -> str:
        """
        Only add new books; raise error if book_name exists
        ratings must be between 0 and 5
        """
        if not isinstance(book_name, str):
            raise TypeError("book_name must be of type String.")
        if not isinstance(rating, int):
            raise TypeError("rating must be of type Integer.")
        if  not 0 <= rating <= 5:
            raise ValueError("rating is not between 0 and 5")
        if len(self.book_list[self.book_list['book_name'].isin([book_name])]):
            
            # Requested book_name already exists in the self.book_list DataFrame
            return f"EXISTS: {book_name} already exists in the book list"
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})

        self.book_list:pd.DataFrame = pd.concat([self.book_list, new_book], ignore_index=True)
        
        return f"ADDED: {book_name} and rating: {rating} has been added to the book list"
    
    # Instance method has_read
    def has_read(self, book_name: str) -> bool:
        """
        Does requested book exist? If not in list raise error
        """
        #print(f"DEBUG:  {len(self.book_list.loc[self.book_list['book_name'] == book_name])}")
        if len(self.book_list[self.book_list['book_name'].isin([book_name])]):
            # Requested book_name exists in the self.book_list DataFrame
            return True
    
        return False
    
    # Instance method num_books_read
    def num_books_read(self) -> int:
        """
        Returns the number of books read
        """
        self.num_books = len(self.book_list)
        return self.num_books
    
    # Instance method fav_books
    def fav_books(self) -> pd.DataFrame:
        """
        returns the filtered dataframe of the person’s most favorite books.
        Books in this list should have a rating > 3.
        """
        
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':


    # Create variable to capture results when necessary
    results: str = ""
    # Instantiate the BookLover class
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    results = myInstance.add_book("War of the worlds", 4)
    print(results)
    results = myInstance.add_book("Embrace the Challenge", 5)
    myInstance.has_read("Embrace the Challenge")
    print(results)
    results = myInstance.add_book("Embrace the Challenge", 5)
    
    print(results)
    print(f"Reader's favorite books: {myInstance.fav_books()}")

    newDataFrame: pd.DataFrame = myInstance.fav_books()
    all3s: bool = (newDataFrame['book_rating'] > 3).all()
    #print(newDataFrame[newDataFrame['book_rating'] < 3])
    print(f"Do all books in the list have a rating > 3? Response: {all3s}")


    # Access instance attributes
    print(myInstance.num_books)

    # Call instance method num_books_read
    print(myInstance.num_books_read())

    num_args = 3
    assert num_args == 3, "number of arguments must be 3!"
    