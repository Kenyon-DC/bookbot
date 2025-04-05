from stats import total_words, letter_count, get_book_text, sort_count
import sys

def main():
    
    if len(sys.argv) < 2 or len(sys.argv) >2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    text = sys.argv[1]
    num_words = total_words()
    letter_total = letter_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_count(letter_total):
        c = item["char"]
        n = item["count"]
        if c.isalpha():
            print(f"{c}: {n}")
    print("============= END ===============")

main()
