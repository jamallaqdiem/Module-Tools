import sys

show_all_numbers = "-n" in sys.argv #  this check will return true if found the flag
show_non_blank_numbers = "-b" in sys.argv #  this check will return true if found the flag

# 2. using filter get only the filenames everything except the script name and flags
files = [arg for arg in sys.argv[1:] if arg not in ["-n", "-b"]]

if not files:
    print("Usage: python3 cat.py [-n] [-b] <filenames>")
    sys.exit()

line_count = 1
# 3. Process each file 
for filename in files:
    try:
        with open(filename, "r") as file:
            for line in file:
                # Logic for -b 
                if show_non_blank_numbers:
                    if line.strip(): # If line is not empty
                        print(f"{line_count:>6}\t{line}", end="")
                        line_count += 1
                    else:
                       # Standard cat no flags
                        print(line, end="")
                
                # Logic for -n 
                elif show_all_numbers:
                    print(f"{line_count:>6}\t{line}", end="")
                    line_count += 1
                
                # Standard cat no flags
                else:
                    print(line, end="")
                    
    # throw clear errors                
    except FileNotFoundError:
        print(f"Error: {filename}: No such file or directory")
    except IsADirectoryError:
        print(f"Error: {filename}: Is a directory")
