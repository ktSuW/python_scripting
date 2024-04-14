import os
import logging 
from collections import Counter
from typing import Dict 

"""
Notes
==================


"""
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_customer_data(filepath: str) -> Dict[str,int]:
    """
    Loads and counts occurrences of customer names from a given file
    Args:
        filepath (str): Path to the file containing customer data.

    Returns:
        Dict[str,int]: A dictionary with customer names as keys and their counts as values
    """
    try:
        customers = Counter()
        with open(filepath, 'r') as file:
            for line in file:
                customer_name = line.split(',')[0].strip()
                customers[customer_name] += 1
        return customers
    except FileNotFoundError:
        logging.error(f'The file {filepath} was not found.')
        raise
    except IOError as e:
        logging.error(f'An I/O error occurred: {e}')
        raise
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise
    
def main():
    """Main function to process customers data
    """
    try:
        dir_path_for_file = os.path.dirname(os.path.abspath(__file__))
        filename = 'customers2.txt'
        filename = os.path.join(dir_path_for_file, filename)
        
        if os.path.normpath(filename) != filename:
            raise ValueError("Invalid file path detected!")
        
        customers = load_customer_data(filename)
        print(customers)
    except Exception as e:
        logging.error(f'Failed to process customer data{e}')
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
#=================================
# # Counter - https://www.geeksforgeeks.org/python-collections-module/
# # With sequence of items
# print(Counter(['A', 'A', 'B','C', 'C', 'B', 'A']))

# # with dictionary
# print(Counter({'A':3, 'B' : 5, 'C':3}))

# # with keyword arguments
# print(Counter(A=3, B=4, C=7))