# Question 4: Indexing and slicing for weekly borrowing statistics
# CS 1101 Unit 5 - Sadman Mubassir Jarif

# Books borrowed each week (week 1 through week 7)
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original weekly borrowing list:")
print(borrowed_books)

# Extract records from week 2 to week 5 using slicing
# Index 1 is week 2; index 4 is week 5; slice [1:5] stops before index 5
weeks_2_to_5 = borrowed_books[1:5]
print("\nBooks borrowed from week 2 to week 5:")
print(weeks_2_to_5)

# Replace the number of books borrowed in week 1 with 20 using indexing
# Week 1 is at index 0
borrowed_books[0] = 20
print("\nUpdated list after changing week 1 to 20:")
print(borrowed_books)

print("\nSliced portion (week 2 to week 5) again:")
print(borrowed_books[1:5])
