from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_dict

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_num_char(book_text)
    sorted_char = get_sorted_dict(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for i in sorted_char:
        print(f"{i['char']}: {i['num']}")
    print("============= END =============") 

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()