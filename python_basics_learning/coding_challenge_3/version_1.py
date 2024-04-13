# version 1

import os 

def get_file_path(filename):
    dir_path_for_file = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_path_for_file, filename)

def load_points(filename):
    points = {}
    filename = get_file_path(filename)
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    # to split ['E', '1 point'] and unpack the variables into two variables
                    letter, point = line.split(':')
                    # Make dictionary - clean up spaces and make letter as key
                    # Adding to points dictionary 
                    points[letter.strip()] = int(point.split()[0])
    except FileNotFoundError:
        print("Error: The file does not exist")
    except Exception as e:
        print(f"An error occured: {e}")
    return points

def get_user_input(points):
    words_scores = []
    total_points = 0
    
    while True:
        word = input(f"Enter a word (or 'quit' to exit): ").upper()
        if word == 'QUIT':
            break
        if not word.isalpha():
            print("Word must contain only alphabets. Please enter only alphabets.")
            continue 
        word_points = sum(points.get(letter, 0) for letter in word)
        words_scores.append((word, word_points))
        total_points +=  word_points
        print(f"Points for {word} : {word_points}")
    return words_scores, total_points

def print_total_points_summary(word_scores, total_points):
    print("\nSummary of entered words and their points:")
    for i, (word, score) in enumerate(word_scores, 1):
        print(f"{i}. {word} - {score} points")
    print(f"Total points: {total_points}")    

def main():
    points = load_points("points.txt")
    word_scores, total_points = get_user_input(points)
    print_total_points_summary(word_scores, total_points)
    

        
if __name__ == "__main__":
    main()  
    
"""
Python OS module - provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality.

with open
open() takes three 3 parameters
- filename
- mode
- encoding 

strip() - removes any leading and trailingwhitespace characters including new lines and spaces from the string letter, to make sure they key used in the dictionary does not include unwanted spaces that might affect the key lookup later

- OOP
- Design Pattern - Singleton Pattern, Command Pattern
    
"""
# print("Current Working dir: ", os.getcwd())
# # Ask question
# points_file= open("points.txt", "r")
# print(points_file.read())
# points_file.close()

# with statement calls 2 built-in methods behind the scenes
# __enter()__ 
# __exit()__
# w - write only, not readable
# r - readble ONLY
# r+ read and write
# with open("hello.txt", "w") as file:
#     file.write("Hello World\n")
#     file.write("Today is a wonderful day!")
#     # with this, you will get UnsupportedOperation: not readable error
#     for line in file:
#         print(line)
# # with open("hello.txt", "r") as file:
# #     for line in file:
# #         print(line)
# a append, r read, w write, w+ read and write even if the file does not exist
#===================================================
# with open("hello.txt", "r+") as file:
#     file.write("Learning OS\n")
#     file.write("New TV series!!\n")
#     # Move the file pointer to the beginning of the file
#     file.seek(0)
#     for line in file:
#         print(line)
    