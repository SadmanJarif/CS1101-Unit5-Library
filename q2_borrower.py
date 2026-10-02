# Question 2: Immutable borrower details with a tuple
# CS 1101 Unit 5 - Sadman Mubassir Jarif

# Create a tuple for one borrower's personal details
# (name, library ID, membership date)
borrower = ("John Doe", "B1023", "2025-10-15")
print("Borrower details (tuple):")
print(borrower)

# Try to modify one element and observe the result
print("\nTrying to change the name in the tuple...")
try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Result: TypeError -", error)
    print("Observation: Tuples are immutable, so items cannot be changed.")

# Print the length and display each element using a loop
print("\nNumber of data fields (len):", len(borrower))
print("Each field in the tuple:")
for item in borrower:
    print("-", item)
