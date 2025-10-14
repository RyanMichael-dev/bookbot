def get_num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def get_num_char(text):
    char_dict = {}
    words = text.lower()
    for char in words:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict