#Write a Python function convert_to_uppercase that:
def convert_to_uppercase(strings):
    return list(map(lambda s: s.upper(), strings))  
words = ["amazing", "mysterious", "furious", "divine"]
uppercase_words = convert_to_uppercase(words)
print(uppercase_words)


#Write a function process_file_with_lambda that:
def process_file_with_lambda(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    processed_lines = []
    for line in lines:   
        words = line.split()  
        upper_words = [word.upper() for word in words]  
        processed_line = ' '.join(upper_words)  
        processed_lines.append(processed_line)

    with open(filename, 'w') as file:
        for processed_line in processed_lines:
            file.write(processed_line + '\n')


