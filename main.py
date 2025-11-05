from stats import get_num_words, get_num_char, get_sorted, sort_on
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    sorted = get_sorted(num_char)
    sorted.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for s in sorted:
        print(f"{s["char"]}: {s["num"]}")
    print("============= END ===============")





def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

