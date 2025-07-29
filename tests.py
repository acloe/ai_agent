from functions.get_files_info import *
from functions.get_file_content import *
'''
print("Result for current directory:")
result1 = get_files_info("calculator", ".")
print(result1)

print("Result for current directory:")
result2 = get_files_info("calculator", "pkg")
print(result2)

print("Result for current directory:")
result3 = get_files_info("calculator", "/bin")
print(result3)

print("Result for current directory:")
result4 = get_files_info("calculator", "../")
print(result4)
'''

print("Result for current directory:")
result5 = get_file_content("calculator", "lorem.txt")
print(result5)

print("File Content:")
result6 = get_file_content("calculator", "main.py")
print(result6)

print("File Content:")
result7 = get_file_content("calculator", "pkg/calculator.py")
print(result7)

print("File Content:")
result8 = get_file_content("calculator", "/bin/cat")
print(result8)

print("File Content:")
result9 = get_file_content("calculator", "pkg/does_not_exist.py")
print(result9)
