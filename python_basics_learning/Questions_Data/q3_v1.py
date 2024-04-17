# Question-3 version 1

import os
import json
from pprint import pprint

def get_file_path(filename):
    dir_path_for_file = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_path_for_file, 'cust_dept.txt')

def group_customers_by_department(cust_dept_filename):
    cust_dept_filename = get_file_path(cust_dept_filename)
    customers_group = {}
    with open(cust_dept_filename, 'r')as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            # line = line.strip()
            if not line:
                continue
            record = line.rstrip().split(',')
            
            # customer_info = {}
            
            # tuple unpacking , it is tuple of variables on LHS, tuple of values on RHS
            first, last, town, phone,email, department = record 
            
            customer_info = {'first': first, 'last': last, 'town': town, 'phone' : phone, 'email':email }
            
            # customer_info['first'] = first 
            # customer_info['last'] = last 
            # customer_info['town'] = town 
            # customer_info['phone'] = phone 
            # customer_info['email'] = email 
            
            # customer_raw_data_full = record[:5]
            # department = record[5]
            # print("+++++++++++++++++++")
            # print(department)
            
            # Create a customer data in dictionary using dictionary comprehension
            # customer_info = {keys[i] : customer_raw_data_full[i].strip() for i in range(len(keys))}
            
            # customer_info = { k:v for k,v in zip(keys, customer_raw_data_full)}
            # print("=============================")
            # print(customer_info)
            # department = customer_info['department']
            # del customer_info['department']

            # if there is existing department, add the dictionary to that existing list
            # if department in customers_group:
            #     customers_group[department].append(customer_info)
            # else:
            #     customers_group[department] = [customer_info]  
            
            if not department in customers_group:
                customers_group[department] = []
                
            customers_group[department].append(customer_info)
            
    # pprint(customers_group)        
    return customers_group

# Write a function to search the departments 'data' structure above by phone number and return that person's details.
def search_customer_info_by_phone_num(customers_group):
    phone_to_search = input("Enter customer phone number: ")
    for department, customers in customers_group.items():
        for customer in customers:
            if customer['phone'] == phone_to_search:
                return customer
    return "No customer found with that phone number."

def main():
    file_path = get_file_path('cust_dept.txt')
    customers_group = group_customers_by_department(file_path)
    # print(json.dumps(customer_details, indent=3, sort_keys=False))
    customer_details = search_customer_info_by_phone_num(customers_group)
    pprint(customers_group)
    
    
if __name__ == '__main__':
    main()

"""
Question 3) -----------------------------------------------------------------------------------------------------------------

Using the attached input file 'cust_dept.txt' write a program to load the data into a structure called 'data' which groups the people by department. 
The output using a pprint of 'data' should look like the following:-

DEPARTMENTS
{'accounts': [{'email': 'fred@somemail.com',
               'first': 'fred',
               'last': 'flint',
               'phone': '987123',
               'town': 'bedrock'},
              {'email': ' pebbles@somemail.com',
               'first': 'pebbles',
               'last': 'flint',
               'phone': '987124',
               'town': 'bedrock'},
              {'email': 'wilma@somemail.com',
               'first': 'wilma',
               'last': 'flint',
               'phone': '987126',
               'town': 'bedrock'}],
 'returns': [{'email': ' kermit@somemail.com',
              'first': 'kermit',
              'last': 'thefrog',
              'phone': '765123',
              'town': 'the swamp'},
             {'email': 'james@somemail.com',
              'first': 'james',
              'last': 'kirk',
              'phone': '009900',
              'town': 'space'}],
 'shipping': [{'email': 'homer@somemail.com',
               'first': 'homer',
               'last': 'simpson',
               'phone': '432567',
               'town': 'springfield'},
              {'email': ' dino@somemail.com',
               'first': 'dino',
               'last': 'flint',
               'phone': '987125',
               'town': 'bedrock'}]}
        
"""

"""
JSON Module
- this module is used for parsing and pretty-printing JSON data.
- json.dumps() is used to convert the dictionary into a formatted string 
- json.dumps() - convert the dictionary into a JSON-format string.
- indent=3 or 4 spaces for each level
- sort_keys=False ensures that the keys are printed in the order they are added to the dictionary

"""