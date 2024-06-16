def copy_file(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as f_source:
            
            content = f_source.read()

        
        with open(destination_file, 'w') as f_dest:
            

        print(f"File '{source_file}' copied successfully to '{destination_file}'.")
    
    except FileNotFoundError:
        print(f"Error: One or both files not found.")
    
    except IOError:
        print(f"Error: Failed to copy '{source_file}' to '{destination_file}'.")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)