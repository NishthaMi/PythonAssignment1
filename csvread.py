import csv

def read_csv_file(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: Failed to read from file '{file_path}'.")

# Example usage:
file_path = 'data.csv'
read_csv_file(file_path)