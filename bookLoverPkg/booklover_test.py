from booklover import BookLover
import unittest


# Create variable to capture results when necessary
results: str = ""

class BookLoverTestSuite(unittest.TestCase):
  
  def test_1_add_book(self): 
    # add a book and test if it is in `book_list`.
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    myInstance.add_book("Return of the Jedi", 4)  # Add a book
    self.assertTrue( myInstance.has_read("Return of the Jedi") )  # Return value should be true
        

  def test_2_add_book(self):
    # add the same book twice. Test if it's in `book_list` only once.
    
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    myInstance.add_book("Return of the Jedi", 4)  # Add a book
    myInstance.add_book("The Force Awakens", 4)  # Add the same book
    results = myInstance.add_book("Return of the Jedi", 4)  # Add the same book
    self.assertTrue("EXISTS" in results)  # Return value should be true
                
  def test_3_has_read(self): 
    # pass a book in the list and test if the answer is `True`.
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    myInstance.add_book("Return of the Jedi", 4)  # Add a book
    myInstance.add_book("The Force Awakens", 5)  # Add another book
    self.assertTrue(myInstance.has_read("Return of the Jedi"))  # Return value should be true
    
        
  def test_4_has_read(self): 
    # pass a book NOT in the list and use `assert False` to test the answer is `True`
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    results = myInstance.add_book("Return of the Jedi", 4)  # Add a book
    results = myInstance.add_book("The Force Awakens", 5)  # Add another book

    self.assertFalse(myInstance.has_read("Return of the Integer"))  # Return value should be true
        
  def test_5_num_books_read(self): 
    # add some books to the list, and test num_books matches expected.
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    myInstance.add_book("Return of the Jedi", 4)  # Add a book
    myInstance.add_book("The Force Awakens", 5)  # Add another book
    myInstance.add_book("Finding Garage Space for the Milleniium Falcon", 2)  # Add another book
    myInstance.add_book("May the Force be with you", 5)  # Add another book
    myInstance.add_book("Vegetables in Space", 2)
    myInstance.add_book("Princess Laia has a bad hair day", 4)
    expectedCount: int = 6
    actualCount: int = myInstance.num_books_read()

    self.assertEqual(actualCount, expectedCount, "Counts Match!")

  def test_6_fav_books(self):
    # add some books with ratings to the list, making sure some of them have rating > 3. 
    # Your test should check that the returned books have rating  > 3
    myInstance: BookLover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #Create an instance
    myInstance.add_book("Return of the Jedi", 4)  # Add a book
    myInstance.add_book("The Force Awakens", 5)  # Add another book
    myInstance.add_book("Finding Garage Space for the Milleniium Falcon", 2)  # Add another book
    myInstance.add_book("May the Force be with you", 5)  # Add another book
    myInstance.add_book("Vegetables in Space", 2)
    myInstance.add_book("Princess Laia has a bad hair day", 4)
    myInstance.add_book("Welcome to the world of EWOKS!", 3)

    newDataFrame: pd.DataFrame = myInstance.fav_books()
    self.assertTrue( (newDataFrame['book_rating'] > 3).all(), "All books in this list have a rating > 3" )


if __name__ == '__main__':
    unittest.main(verbosity=3)