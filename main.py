
from stats import number_of_words, character_usage, sort_usage

def get_book_text(rel_path):
    with open(rel_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    usage = character_usage(book_text)
    sorted_usage = sort_usage(usage)
    for pair in sorted_usage:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()