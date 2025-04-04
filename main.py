from stats import get_word_count,create_word_count_dictionary,create_word_list_dict
import sys

def get_book_text(input_path):
    with open(input_path) as f: 
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    words = get_book_text(path)
    print(f"Analyzing book found at {path}")
    print('----------- Word Count ----------')
    word_count = get_word_count(words)
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    print(f"{word_count} words found in the document")
    word_dict = create_word_count_dictionary(words)
    new_list = create_word_list_dict(word_dict)
    for word_dict in new_list:
        if not word_dict["char"].isalpha():
            continue
        print(f'{word_dict["char"]}: {word_dict["count"]}')
    print('============= END ===============')


main()

