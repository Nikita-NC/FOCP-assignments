"""Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used."""
import sys

def main():
    print(f"The operating system platform being used is : {sys.platform}")

if __name__ == "__main__":
    main()   