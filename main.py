from stats import get_num_words
from stats import get_num_char

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    char_count = get_num_char(book_text)
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()