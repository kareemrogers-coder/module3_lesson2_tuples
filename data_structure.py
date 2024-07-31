
####Question 2


# Objective: This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.


# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.


# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).



library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_tup = ("1984", "George Orwell") #### used this line to change the title and author of the book.

if new_tup in library:
    print("Book already exist in your library")
else:
    library += new_tup
    print(f"New Book alert!!!! listed are the book list inside your library: {library}")


