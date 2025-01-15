"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""
temperature = []

while True:
    user_input = input("Enter temperature: ")
    
    if user_input == "":
        break

    temperatures = float(user_input)
    temperature.append(temperatures)

if temperature:

    max_temp = max(temperature)
    min_temp = min(temperature)
    sum_temp = max_temp + min_temp
    mean_temp = sum(temperature) / len(temperature)

    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"sum of temperature: {sum_temp}")
    print(f"Mean temperature: {mean_temp}")
else:
    print("Temperatures not entered.")
