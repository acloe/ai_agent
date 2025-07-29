import os
from functions import config

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return(f'Error: Cannot read "{full_path}" as it is outside the permitted working directory')
    if not os.path.isfile(full_path):
        return(f'Error: File not found or is not a regular file: "{full_path}"')
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
    except Exception as e:
        return(f"Error: Can't read {full_path} {e}")
        
    if os.path.getsize(full_path) > config.MAX_CHARS:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
    return(file_content_string)
    
    
    
    