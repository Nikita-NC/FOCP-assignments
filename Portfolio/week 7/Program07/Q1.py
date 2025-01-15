"""Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']"""

def letters(string):
    return sorted(set(string)) #gives output in set

result = letters("chess") 
print(result)
