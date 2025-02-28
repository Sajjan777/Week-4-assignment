#Write a Python function filter_even_length_words that:
def filter_even_length_words(words):
    return list(filter(lambda word: len(word) % 2 == 0, words))  


word_list = ["class", "home", "pit", "sit", "elegant", "lend"]
even_length_words = filter_even_length_words(word_list)
print(even_length_words)  
