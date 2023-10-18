//AP21110010160


def calculate_similarity(file_path_1, file_path_2):
    with open(file_path_1, 'r', encoding='utf-8') as f1, open(file_path_2, 'r', encoding='utf-8') as f2:
        text_1 = f1.read()
        text_2 = f2.read()

        words_set_1 = set(text_1.split())
        words_set_2 = set(text_2.split())

        common_words_count = len(words_set_1.intersection(words_set_2))
        total_words_count = len(words_set_1) + len(words_set_2)
        similarity_index = common_words_count / total_words_count

    return similarity_index

file_path_1 = 'file1.txt'
file_path_2 = 'file2.txt'

similarity_index = calculate_similarity(file_path_1, file_path_2)

print(f"Similarity Index: {similarity_index:.2%}")
