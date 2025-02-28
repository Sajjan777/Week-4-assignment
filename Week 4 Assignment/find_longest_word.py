def find_longest_word(file_path):
    with open(file_path, 'r') as file:  
        words = file.read().split() 
    
    if not words: 
        return None  
    return max(words, key=len) 
file_path = "example.txt" 
longest_word = find_longest_word(file_path)

if longest_word:
    print("Longest word:", longest_word)
else:
    print("The file is empty.")
