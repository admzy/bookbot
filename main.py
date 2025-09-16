from stats import count_words
from stats import toLower
from stats import counting_letters
from stats import sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = count_words(text) #this counts the words 
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print ("Found", words, "total words")
    print("--------- Character Count -------")
    counting = toLower(text) #splits the text and counts the characters
    #sorted_ready is var name, counting_letters is the function - counting is the result of previous function that produces a list of characters
    sorted_ready = counting_letters(counting) 
    sorted_ready.sort(key=sort_on, reverse=True) #sorting
    for item in sorted_ready: 
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()