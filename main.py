import os
import random
import uuid

def create_random_files(num_files, min_size_mb=1, max_size_mb=10, directory="random_files"):
    """
    Creates a specified number of files with random names and random content.
    
    :param num_files: Number of files to create
    :param min_size_mb: Minimum size of each file in MB
    :param max_size_mb: Maximum size of each file in MB
    :param directory: Directory where files will be created
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(num_files):
        # Generate a random file name
        file_name = f"{uuid.uuid4()}.bin"
        file_path = os.path.join(directory, file_name)
        
        # Determine a random file size between 1 and 5 MB
        file_size = random.randint(min_size_mb, max_size_mb) * 1048576  # Convert MB to bytes
        
        # Generate random content for the file
        with open(file_path, "wb") as f:
            f.write(os.urandom(file_size))
        
        print(f"Created {file_name} with size {file_size / (1024 * 1024):.2f} MB")


create_random_files(num_files=100)
