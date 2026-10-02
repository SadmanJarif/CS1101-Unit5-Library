# Question 1: Managing a list of library book titles
# CS 1101 Unit 5 - Sadman Mubassir Jarif

# Create a list of book titles available in the library
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Original list of books:")
print(books)

# Add two more books using append()
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")
print("\nAfter adding two books:")
print(books)

# Remove one damaged book using remove()
books.remove("Moby Dick")
print("\nAfter removing the damaged book 'Moby Dick':")
print(books)

# Sort the list alphabetically and display the final list
books.sort()
print("\nFinal sorted list of books:")
print(books)
