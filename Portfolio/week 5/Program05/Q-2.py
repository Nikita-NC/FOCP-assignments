"""Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument)."""
import sys

def main():
    number_argv = len(sys.argv) -1  #to get the number of argument, subtracting 1 form length of sys.argv 
    print(number_argv)

if __name__ == "__main__":
    main()    