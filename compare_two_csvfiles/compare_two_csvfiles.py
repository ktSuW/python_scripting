import pandas as pd
import os

def compare_csv_files(file1_path, file2_path, output_path):
    # Read the CSV files into DataFrames
    file1_df = pd.read_csv(file1_path)
    file2_df = pd.read_csv(file2_path)

    # Find rows that are in file1_df but not in file2_df
    file1_diff = file1_df[~file1_df.apply(tuple, 1).isin(file2_df.apply(tuple, 1))]
    # Find rows that are in file2_df but not in file1_df
    file2_diff = file2_df[~file2_df.apply(tuple, 1).isin(file1_df.apply(tuple, 1))]

    # Write the differences to a text file
    with open(output_path, 'w') as output_file:
        output_file.write(f"Rows in {file1_df} but not in {file2_df}:\n")
        output_file.write(file1_diff.to_string(index=False))
        output_file.write("\n\n")
        
        output_file.write(f"Rows in {file2_df} but not in {file1_df}:\n")
        output_file.write(file2_diff.to_string(index=False))

def run_comparison():
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_dir, 'input', 'BGL_log_1.csv')
    file2_path = os.path.join(current_dir, 'input', 'BGL_log_2.csv')
    output_path = os.path.join(current_dir, 'differences.txt')
    
    # Call the function to compare files and generate the report
    compare_csv_files(file1_path, file2_path, output_path)

if __name__ == "__main__":
    run_comparison()
