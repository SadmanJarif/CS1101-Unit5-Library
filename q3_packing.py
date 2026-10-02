# Question 3: Tuple packing and unpacking for book information
# CS 1101 Unit 5 - Sadman Mubassir Jarif

# Pack a book title, author, and publication year into a tuple
book_info = ("The Alchemist", "Paulo Coelho", 1988)
print("Packed tuple book_info:")
print(book_info)

# Unpack the tuple into separate variables
title, author, year = book_info

# Print them in a readable format
print("\nUnpacked book information:")
print("Title:", title)
print("Author:", author)
print("Year:", year)

# Explanation (also discussed in the written report)
print("\nNote: Packing stores related values together.")
print("Unpacking gives each value a clear name for easy use.")
