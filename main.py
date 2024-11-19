def main ():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    return words

def sort_on_value(item):
    return item[1]

def character_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        lowercase_file_contents = file_contents.lower()
        # remove all the spaces in the text
        lowercase_file_contents = lowercase_file_contents.replace(" ", "")
        character_count = {}
        if lowercase_file_contents:
            for char in lowercase_file_contents:
                if char.isalpha():
                    if char in character_count:
                        character_count[char] += 1
                    else:
                        character_count[char] = 1
        
        print ("--- Begin report of books/frankenstein.txt ---")
        print (len(words), "words found in the document")

        sorted_char_count = sorted(character_count.items(), key=sort_on_value, reverse=True)
        for char, count in sorted_char_count:
            print (f"The '{char}' character was found {count} times")

        print ("--- End report ---")
    

character_count()