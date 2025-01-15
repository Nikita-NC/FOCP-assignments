"""Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program"""

def list_of_countries():
    countries = []

    while True:
        country = input("Enter a country or 'exit' to quit: ").strip() #strip is used to remove unwanted space, tab or newlines for string
        if country.lower() == 'exit':
            break
        
        for c, capital in countries:
             if c.lower() == country.lower():
                print(f"The Capital of {country} is {countries[country]}.")
                break

        else:
            capital = input(f"What is the capital of {country}? ").strip()
            countries.append((country,capital)) #inner () is to create tuple
            print(f"{capital} has been added as the capital of {country}.")

list_of_countries()
