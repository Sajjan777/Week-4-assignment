def read_file_content(file_path):
    with open(file_path, 'r') as file:  
        content = file.read() 
    return content  
def write_to_file(file_path, content):
    with open(file_path, 'w') as file: 
        file.write(content) 
file_path = "example.txt"

write_to_file(file_path, "Hello, I am Sajjan Raj Malla Thakuri")
content = read_file_content(file_path)

print(content)
