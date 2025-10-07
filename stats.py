def num_of_words_in_string(str):
    words_list = str.split()
    return len(words_list)

def num_of_letters_in_string(str):
    letters_dict = {}
    lower_case_str = str.lower()
    for c in lower_case_str:
        if c in letters_dict:
            letters_dict[c] += 1
        else:
            letters_dict[c] = 1

    return letters_dict

def sort_on(items):
    return items["num"]
#{"char": "b", "num": 4868}
def dict_into_list_of_dicts(letters_dict):
    letters_list = []
    for letter in letters_dict:
        dict = {}
        dict["char"] = letter
        dict["num"] = letters_dict[letter]
        letters_list.append(dict)
    
    #print(letters_dict)
    letters_list.sort(reverse=True, key=sort_on)
    #print("\n\n\n\n\n\n\n")
    #print(letters_list)
    #print("\n\n\n\n\n\n\n")
    return letters_list