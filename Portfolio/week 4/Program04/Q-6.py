"""Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""
input_temp = input("Enter the temperatuure in celsius:")

if input_temp[-1].upper()=='C':

    celsius = float(input_temp[:-1])
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{fahrenheit:.2f}F")

else:
    print("invalid format")    