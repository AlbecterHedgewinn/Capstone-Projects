### Create a Class for an Author ###
### Daniel Bittner September 8 2025 ###


# An Author has a name, and a list of books published.
# When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
# Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
# Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
# Write a main function to test your class, create some example authors, and publish some example books. 

# Define the Author class
# Keep in mind that an author can publish multiple books.
# __init__ method initializes the author's name and an empty list of books.
# publish method adds a book title to the author's list of books.
# __str__ method returns a string representation of the author and their books.
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        books_str = ', '.join(self.books) if self.books else 'No books published'
        return f'Author: {self.name}, Books: {books_str}'
    

# Example Data Insertion
# author1 and author2 are instances of the Author class.
# Use Publish method to add books to each author.
# Print the string representation of each author to see their details.
def main():
    author1 = Author("J.K. Rowling")
    author2 = Author("George R.R. Martin")

    author1.publish("Harry Potter and the Sorcerer's Stone")
    author1.publish("Harry Potter and the Chamber of Secrets")
    
    author2.publish("A Game of Thrones")
    author2.publish("A Clash of Kings")

    print(author1)
    print(author2)

# Run the main function
main()