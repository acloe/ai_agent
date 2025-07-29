from functions.get_files_info import get_files_info

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