def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read from: ")  
        # Open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()  # Modify as needed
        # Ask for the new filename to write the modified content to
        new_filename = input("Enter the filename to write the modified content to: ")
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)  
        print("File has been modified and saved to", new_filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print("Error: An error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Call the function
read_and_write_file()
