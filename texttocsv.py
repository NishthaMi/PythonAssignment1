def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as f_source:
            # Read the entire content of the source file
            content = f_source.read()

        # Open the destination file for writing
        with open(destination_file, 'w') as f_dest:
            # Write the content to the destination file
            f_dest.write(content)

        print(f"File '{source_file}' copied successfully to '{destination_file}'.")
    
    except FileNotFoundError:
        print(f"Error: One or both files not found.")
    
    except IOError:
        print(f"Error: Failed to copy '{source_file}' to '{destination_file}'.")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)