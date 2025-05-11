import sys

from stats import get_num_words, count_chars, list_dict_char


def get_book_text(filepath) -> str:
    content = None
    with open(filepath) as f:
        content = f.read()

    return content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = sys.argv[1]
    book_string = get_book_text(book)
    print(f"Analyzing book found at {book}...")

    print("----------- Word Count ----------")
    word_count = get_num_words(book_string)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    count_dict = count_chars(book_string)
    list_dict_char(count_dict)
    print("============= END ===============")
