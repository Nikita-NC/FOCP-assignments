"""Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values."""
temperature = []

for i in range(6):
    temp = float(input(f"Enter temperature {i+1}: "))
    temperature.append(temp)

max_temp = max(temperature)
min_temp = min(temperature)
sum_temp = max_temp + min_temp 
mean_temp = sum_temp / len(temperature)

print(f"maximum temperature: {max_temp}")
print(f"minimum temperature: {min_temp}")
print(f"sum of temperature: {sum_temp}")
print(f"mean temperature: {mean_temp:.2f}")