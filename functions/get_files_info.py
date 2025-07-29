import os
def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
   
    if not os.path.isdir(full_path):
        return (f'Error: "{full_path}" is not a directory')
    
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    directory_file_listing = ""
    
    for file in (os.listdir(full_path)):
        files_skipped = ('.', '__')
        if not file.startswith(files_skipped):
            file_path = os.path.join(full_path, file)
            try:
                file_size = os.path.getsize(file_path)
            except:
                return(f"Error: Unable to get file_size for file {file_path}")
            try:
                file_is_dir = os.path.isdir(file_path)
            except:
                return(f"Error: Not able to determine if {file_path} is a directory")
            directory_file_listing = directory_file_listing + f"- {file}: file_size={file_size} bytes, is_dir={file_is_dir}\n"
    return(directory_file_listing)