from functions.run_python_file import run_python_file

print("Result for main.py file:")
print(run_python_file("calculator", "main.py"))

print("Result for calculator using main.py file:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Result for tests.py file:")
print(run_python_file("calculator", "tests.py"))

print("Result for nested main.py file:")
print(run_python_file("calculator", "../main.py"))

print("Result for nonexistent.py file:")
print(run_python_file("calculator", "nonexistent.py"))

print("Result for lorem.txt file:")
print(run_python_file("calculator", "lorem.txt"))