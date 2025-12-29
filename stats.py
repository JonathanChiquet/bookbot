# Word counter function that sends the total numbers in the text
def word_counter(book):
    words = book.split()
    return len(words)

# Letter counter function that shows the quantity of each letter inside the text
def char_counter(book):
    times_each_char = {}
    lowered_text = book.lower()

    for char in lowered_text:
       if char.isalpha():
            if char in times_each_char:
               times_each_char[char] += 1
            else:
                times_each_char[char] = 1
    
    return times_each_char

# Sort function that change the order from most repetitive letter to the least
def sort_char(chars):
    chars_list = []

    for char, count in chars.items():
        chars_dict = {"char": char, "num": count}
        chars_list.append(chars_dict)
    
    def sort_on(items):
        return items["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
