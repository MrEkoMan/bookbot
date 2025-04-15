def word_count(text):
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    # Split the text into words and return the count.
    return len(text.split())

def char_count(text):
    """
    Count the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dictionary: The letter and number of occurances in the text.
    """

    # Remove punctuation and special characters from the text.
    text = ''.join(filter(str.isalpha, text)).lower()
    # Create a dictionary to store the character counts.
    counts = {}
    
    # Iterate through each character in the text.
    for char in text:
        # If the character is alphanumeric, update its count.
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    
    return counts