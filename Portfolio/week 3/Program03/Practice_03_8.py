"""Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times"""

num=int(input("Enter the number: "))

if num>=0:
    for x in range(0,13):
        print(f"{x} x {num} = {x*num}")

else:        
    for x in range(12,-1,-1):
        print(f"{x} x {-num} = {x*-num}")    