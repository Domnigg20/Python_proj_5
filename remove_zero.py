##Python code to remove zeros from a sample txt file

def remove_zeros(input_file, output_file):
    with open(input_file, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Remove zeros from the content
        content_without_zeros = content.replace('0', '')

    with open(output_file, 'w') as file:
        # Write the modified content to the output file
        file.write(content_without_zeros)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_file_path = "input.txt"
    output_file_path = "output.txt"

    # Call the remove_zeros function
    remove_zeros(input_file_path, output_file_path)

    print(f"Zeros removed from {input_file_path}. Output saved to {output_file_path}.")
