import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
from stats import get_word_count, count_characters, sort_dicts

def main():
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = count_characters(book_text)
    sorted_dicts_list = sort_dicts(char_count)
    
    message = f"""============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------"""
    for char_dict in sorted_dicts_list:
        character = char_dict["character"]
        number = char_dict["number"]
        message += f"\n    {character}: {number}"
    message += f"\n============= END ==============="
    print(message)    



main()