def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    lowercase = text.lower()
    characters = list(lowercase)
    character_count = {}
    for character in characters:
        if character in character_count:
            character_count [character] += 1
        else:
            character_count[character] = 1
    return character_count


def sort_dicts(input_dictionary):
    dict_list = []
    for character, count in input_dictionary.items():
        if character.isalpha() == True:
            dict_list.append({"character": character, "number": count})
     
    dict_list.sort(reverse=True, key=lambda x: x["number"])
    
    
    return dict_list
    