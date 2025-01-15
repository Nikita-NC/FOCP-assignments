"""Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code"""
from sys import argv
from urllib.request import urlopen
from urllib.error import*

try:
    user_link = argv [1]
    link = urlopen(user_link)
except IndexError as i:
    print("No url provided and",1)
except HTTPError as h:
    print("HTTP error",h)
except URLError as u:
    print("Opps page not found ",u)
else:
    print("Page found")          