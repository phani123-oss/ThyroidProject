import os
#used this code to overcome the error that i have while running second time 
#error occurs because of prediction_artifacts and predictions already created after firsttime running

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

# Ensure the directory exists before file operations
def perform_file_operations():
    ensure_directory_exists('prediction_artifacts')

    # Define file paths
    file_path = os.path.join('prediction_artifacts', 'some_file.txt')

    # Check if the file exists before accessing it
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist. Creating file.")
        with open(file_path, 'w') as f:
            f.write("Initial content.")

# Call the function that performs file operations
perform_file_operations()
