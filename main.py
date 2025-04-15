from stats import *
import sys

def get_book_text(filepath):
    """
    Read the content of a book file and return it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    # Open the file in read mode with UTF-8 encoding
    # and return its content as a string.
    contents = ""

    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read() 

    return contents


def main():
    """
    Main function to execute the book reading process.
    
    This function prompts the user for a book file path,
    retrieves the book text, and prints it.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Prompt the user for the book file path.
    filepath = sys.argv[1]

    #filepath = "books/frankenstein.txt"
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at: {}...".format(filepath))
    
    # Get the book text from the specified file.
    book_text = get_book_text(filepath)
    
    print("----------- Word Count -----------")
    count = word_count(book_text)
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    dict = char_count(book_text)
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_dict:
        print("{}: {}".format(k,v))

main()
