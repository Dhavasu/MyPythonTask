def read_file(file_path):
    with open(file_path, 'r') as file:
        print(f"File '{file_path}' written with initial content.\n")
        return file.read()
    
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print(f"Additional content appended to '{file_path}'.\n")
        

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = "todayclasslist.txt"
initial_content = "Welcome to the class.\nThis is the present list.\n"
additional_content = "This is an absent list.\n"
