"""
Coding Challenge 1: Restaurant Bill Calculator
Scenario: You're out with friends at a restaurant and want to split the bill evenly. Write a Python program that takes the following as input:
Total bill amount: A float (e.g., 50.25)
Number of people splitting the bill: An integer (e.g., 4)
Tip percentage: An integer (e.g., 20)
Output:
Print the individual bill amount per person, including the tip.
Optionally, ask the user if they want to round the individual amount to the nearest whole number and print the rounded amount.
Hints:
Use the input() function to receive user input for each variable.
Convert the string input for the number of people and the tip percentage to integers using the int() function.
Calculate the total tip amount by multiplying the total bill amount by the tip percentage (converted to a decimal) and then dividing by 100.
Calculate the individual bill amount by adding the total tip amount to the total bill amount and then dividing by the number of people.

Use string formatting to display the output with proper labels and precision.
Bonus:
Modify the program to allow for different tip amounts for different people at the table.
Use a loop to read and store individual tip amounts for each person.

"""
import math
def get_float_input(input_value):
    while True:
        try:
            return float(input(input_value))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(input_value):
    while True:
        try:
            return int(input(input_value))
        except ValueError:
            print("Please enter int number.")
            
def print_bills(individual_bills):
    for person,bill in enumerate(individual_bills):
        print(f"The total bill per person {person + 1} is {bill:.2f}")
        
def calculate_average_bill_per_person(individual_bills_list):
    average_bill = sum(individual_bills_list)/ len(individual_bills_list)
    return average_bill

def calculate_restaurant_bill():
    # multiple variable assignemnts 
    total_bill = get_float_input("Enter the total bill: ")
    num_of_people_splitting = get_int_input("Enter the number of people: ")
    
    individual_bills_list = []
    total_tip_amount = 0
    individual_bill= 0
    
    for person in range(num_of_people_splitting):
        tip_percentage = get_float_input(f"Enter tip percentage for person {person + 1}: ")
        individual_tip_amount= total_bill * (tip_percentage/100)
        individual_bill= (total_bill + individual_tip_amount)/num_of_people_splitting 
        individual_bills_list.append(individual_bill)
        total_tip_amount += individual_tip_amount
        
    print_bills(individual_bills_list)
    print(f"The total tip amount for this group group is {total_tip_amount:.2f}")
    print(f"The average bill for each person is {calculate_average_bill_per_person(individual_bills_list):.2f}")
    
def main():
    calculate_restaurant_bill()

if __name__ == "__main__":
    main()


"""
-  range(num_of_people_splitting): This creates a sequence of numbers from 0 to num_of_people_splitting - 1
- enumerate function - https://blog.hubspot.com/website/python-enumerate
- https://realpython.com/python-enumerate/

"""