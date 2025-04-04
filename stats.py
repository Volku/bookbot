
def get_word_count(words):
    return len(words.split())

def create_word_count_dictionary(words):
    str_dict ={}
    for character in words:
        if character.lower() in str_dict:
            str_dict[character.lower()]+=1
            continue
        str_dict[character.lower()]=1
    return str_dict

def create_word_list_dict(dictionary):
    new_list = []
    for key,value in dictionary.items():
        new_list.append({"char":key, "count": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict['count']