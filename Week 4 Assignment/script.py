
def process_file_with_lambda(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(' '.join(map(str.upper, line.split())) + '\n')

process_file_with_lambda("sample.txt")  
