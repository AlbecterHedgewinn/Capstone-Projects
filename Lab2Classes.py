### Create a Class for an Author ###
### Daniel Bittner September 8 2025 ###

# PArt 1------------------------------------------------------
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


# We use a class for an Author because it allows us to encapsulate both the data 
# (author's name and list of books) and the behavior (publishing books and string representation) 
# related to an author in a single structure. This makes the code more organized, 
# reusable, and easier to maintain. Each Author object can manage its own state and behavior, 
# which is a key principle of object-oriented programming.



# Part 2------------------------------------------------------
# Start with the program from part 1.
# In this version, an author can't publish two books with the same name.
# When the publish method is called, print an error message if the book given 
# has the same name as a book currently in the books list. Do not add the duplicate book. 
# (In other words, make sure the Author object's book list doesn't already contain that name).  


# Updated publish method to prevent duplicate book titles.
# The if statement checks if the title is already in the books list.
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print(f"Error: '{title}' has already been published by {self.name}.")
        else:
            self.books.append(title)

    def __str__(self):
        books_str = ', '.join(self.books) if self.books else 'No books published'
        return f'Author: {self.name}, Books: {books_str}'
    

# Alternatively, you could use a set to store book titles, which inherently prevents duplicates.
# However, using a list allows us to maintain the order of publication.



# Part 3------------------------------------------------------
# Write the Student Class from the assigned reading
# Add one more field: gpa, a float.
# Write a main function to create some example Student objects with some example names, 
# college_id and GPA values. Verify you can read the name, college ID and GPA for an example student.  
# Verify when you print an example student, the GPA is included. 

class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, College ID: {self.college_id}, GPA: {self.gpa}'


def main2():
    student1 = Student("Alice", "aa12345aa", 3.8)
    student2 = Student("Bob", "bb1234bb", 3.5)

    print(student1)
    print(student2)

main2()

# When defeining fields in a class, the type of each field is defined by the value assigned to it in the __init__ method.
# in this case, gpa is defined as a float because it is assigned a floating-point number when creating Student objects in
# the main2 function. This allows the gpa field to store decimal values, which is appropriate for representing a student's GPA.