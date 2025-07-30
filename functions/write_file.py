import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    try:
        with open(full_path, "w") as file:
            file.write(content)
    except Exception as e:
        return(f"Error: Can not write to the file {full_path}")
    
    return(f'Successfully wrote to "{full_path}" ({len(content)} characters written)')
        