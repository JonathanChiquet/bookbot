from stats import word_counter, char_counter, sort_char
import sys

# This function returns the filepath (text) in a string for later use
def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()

# Main function that prints the final format    
def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

    filepath = sys.argv[1]    
    book_content = get_book_text(filepath)

    getting_book = word_counter(book_content)
    counting_letter = char_counter(book_content)
    sorted_list = sort_char(counting_letter)

    first_message = print(
    "============ BOOKBOT ============ \n" \
    f"Analyzing book found at {filepath} \n" \
    "----------- Word Count ---------- \n" \
    f"Found { getting_book } total words \n" \
    "--------- Character Count -------")

    for c in sorted_list:
        letter = c["char"]
        counter = c["num"]
        if letter.isalpha():
            print(f"{letter}: {counter}")
        
    last_message = print("============= END ===============")

    return first_message, last_message

main() 