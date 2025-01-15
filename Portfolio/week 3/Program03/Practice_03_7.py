"""Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive."""

num=int(input("Enter the number: "))

for x in range(0,13):
    print(f"{x} x {num} = {x*num}")