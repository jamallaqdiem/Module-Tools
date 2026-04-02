import cowsay
import argparse

# 1. Fetch the animals from the library
list_of_animals = cowsay.char_names

# 2. Setup the Parser, I'm building a program cowsay that to do(description).
parse = argparse.ArgumentParser(prog='cowsay', description='make animals say things')
parse.add_argument('message', nargs='+', help='The message to say')

parse.add_argument('--animal', choices=list_of_animals, default='cow', help='The animal to use')

args = parse.parse_args()

# Combining the words into a single string
message_text = " ".join(args.message)

# we call the draw_function and we use getattr because args.animal is a string, and we need a function instead.
draw_function = getattr(cowsay, args.animal)

# 4. call and execute.
draw_function(message_text)
