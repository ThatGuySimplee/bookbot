from stats import num_words, num_char


def main():
    text = get_book_text("books/frankenstein.txt")
    count = num_words(text)
    char = num_char(text)
    print(f"Found {num_words} total words")
    print(char)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

