//AP21110010160


import re

def count_characters_numbers_words(filename):
    character_count = 0
    number_count = 0
    word_count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            character_count += len(line)
            
            number_count += len(re.findall(r'\d+', line))
            
            words = line.split()
            word_count += len(words)

    return character_count, number_count, word_count

file_path = 'text_file.txt'

char_count, num_count, word_count = count_characters_numbers_words(file_path)

print(f"Number of characters: {char_count}")
print(f"Number of numbers: {num_count}")
print(f"Number of words: {word_count}")
