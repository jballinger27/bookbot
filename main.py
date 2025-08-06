
from stats import number_of_words, character_usage, sort_usage
import sys
def get_book_text(rel_path):
    with open(rel_path) as f:
        return f.read()

def main():
    book_text = ""
    if len(sys.argv) > 1:
        book_text = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"Found {number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    usage = character_usage(book_text)
    sorted_usage = sort_usage(usage)
    for pair in sorted_usage:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()