try:
    file = open("C:/Users/LENOVO/OneDrive/Desktop/Python Assignments/Python-Assignment-4/sample.txt", "r")
    data = file.read()
    file.close()

    print("Reading file content:")
    print(data)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")   