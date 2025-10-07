import sys
from stats import num_of_words_in_string
from stats import num_of_letters_in_string
from stats import dict_into_list_of_dicts

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    
    return file_contents
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    file_contents = get_book_text(f"/root/bookbot/{relative_path}")
    num_of_words_in_file = num_of_words_in_string(file_contents)
    dict_of_letters_in_file = num_of_letters_in_string(file_contents)
    list_of_letters_and_nums = dict_into_list_of_dicts(dict_of_letters_in_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words_in_file} total words")
    print("--------- Character Count -------")
    for dict in list_of_letters_and_nums:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["num"]}')
    print("============= END ===============")
