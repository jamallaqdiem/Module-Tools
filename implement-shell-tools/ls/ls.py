import os
import sys

# assign flags
show_all = "-a" in sys.argv
one_column = "-1" in sys.argv

# Argument Filtering 
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
# if no path given we use the current path
path = args[0] if args else "."

try:
    # Get directory contents
    entries = os.listdir(path)

    # Handle the -a flag 
    if show_all:
        entries.extend([".", ".."])
    
    # 5. Sort alphabetically, should used in ls.js as well
    entries.sort()

    # Printing Logic
    for entry in entries:
        # Skip hidden files unless -a is passed
        if not show_all and entry.startswith("."):
            continue
            
        if one_column:
            # -1 flag: Print vertically
            print(entry)
        else:
            # Standard: Print horizontally with spaces
            print(entry, end="  ")

    #  newline only if we not print horizontally
    if not one_column:
        print()

except FileNotFoundError:
    print(f"ls: cannot access '{path}': No such file or directory")
except NotADirectoryError:
    # if a file  ls just prints the filename
    print(path)
