import sys
from stats import get_num_words, get_num_characters, sorted_characters

def get_book_text(book_path):
    with open(f"{book_path}", "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing books found at {sys.argv[1]}...")
        book_text = get_book_text(sys.argv[1])
        word_count = get_num_words(book_text)
        character_count = get_num_characters(book_text)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        sorted_characters(character_count)
    

if __name__ == "__main__":
    main()
