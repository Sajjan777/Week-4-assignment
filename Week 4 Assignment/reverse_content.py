def reverse_file_content(file_path):
    with open(file_path, 'r') as file: 
        content = file.read() 
    
    with open('reversed.txt', 'w') as reversed_file:  
        reversed_file.write(content[::-1]) 

file_path = "example.txt"  
reverse_file_content(file_path)
print("The reversed content has been saved to reversed.txt.")
