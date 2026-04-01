from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print("Result for Lorem Ipsum text file:")
print(len(result))
print(result.endswith('[...File "lorem.txt" truncated at 10000 characters]'))

print("Result for current file:")
print(get_file_content("calculator", "main.py"))

print("Result for 'pkg/calculator.py' file:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Result for '/bin/cat' file:")
print(get_file_content("calculator", "/bin/cat"))

print("Result for 'pkg/does_not_exist.py' file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))