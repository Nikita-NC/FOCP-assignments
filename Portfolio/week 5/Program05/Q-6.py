"""Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a dierent name
"""
import shutil
import sys

if len(sys.argv) != 2:
    print("Usage: python backup.py <filename>")
else:
    filename = sys.argv[1]
    backup_filename = filename + "_backup"

    shutil.copy(filename, backup_filename)
    print(f"Backup created: {backup_filename}")
