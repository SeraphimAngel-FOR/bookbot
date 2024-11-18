def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    # Get the character counts
    character_counts = count_characters(text)
    
    # Get the sorted counts
    sorted_counts = sorting_script(character_counts)
    
    # Print each character and its count
    print("\nCharacter Counts:")
    for char, count in sorted_counts:
        # Only print if the character is alphabetic
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Create a local dictionary
    character_counts = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts  # Return the dictionary

def sorting_script(character_counts):
    pairs = character_counts.items()
    sorted_by_frequency = sorted(pairs, key=lambda x: x[1], reverse=True)
    return sorted_by_frequency
    

main() 