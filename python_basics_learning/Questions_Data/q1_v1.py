"""
Question 1) 
The attached input file 'customers2.txt' contains duplicated and replicated records. 
Write a program to count the number of times each record appears in the file.
The output should look like the following (first name only):-
{'fred': 1, 'homer': 2, 'kermit': 3, 'james': 2}"""

import os

dir_path_for_file = os.path.dirname(os.path.abspath(__file__))
# print(dir_path_for_file)
filename = os.path.join(dir_path_for_file, "customers2.txt")

customers = {}
with open (filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        each_customer = line.split(',')[0].strip()
            
        if each_customer in customers:
            customers[each_customer] += 1
        else:
            customers[each_customer] = 1
print(customers)
customers_sorted = sorted(customers.items(), key=lambda x:x[1], reverse=True) # return a list of tuples because dictionaries themselves can't be directly ordered
customers_sorted_reconstructed_to_dic = dict(customers_sorted)
print(customers_sorted_reconstructed_to_dic)