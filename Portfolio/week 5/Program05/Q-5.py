"""Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!"""
import sys

if len(sys.argv) < 2:
    print("Please enter temperature values as command line arguments.")
else:
    try:
        temperatures = [float(temp) for temp in sys.argv[1:]]
    except ValueError:
        print("Please enter valid numerical temperature values.")
        sys.exit(1)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    sum_temp = sum(temperatures) 
    mean_temp = sum_temp / len(temperatures)

    print(f"Maximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Sum of Temperatures: {sum_temp}")
    print(f"Mean Temperature: {mean_temp:.2f}")
