"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""
def celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit  = float(input("Enter temperature in Fahrenheit: "))

c_to_f = celsius_to_fahrenheit(celsius)
f_to_c = fahrenheit_to_celsius(fahrenheit)

print(f"{celsius}C is equivalent to {c_to_f:.2f}F ")
print(f"{fahrenheit}F is equivalent to {f_to_c:.2f}C")