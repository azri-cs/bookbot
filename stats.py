def calc_characters(text):
        char_counts = {}
        lowered_text = text.lower()
        for char in lowered_text:
                if char in char_counts:
                        char_counts[char] += 1
                else:
                        char_counts[char] = 1
        return char_counts

def calc_words(text):
	return len(text.split())

def get_list_of_dictionaries(text):
	chars_dict = calc_characters(text)
	chars_tuples = chars_dict.items()
	sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)

	return sorted_chars
