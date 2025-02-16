def calc_words(text):
	return len(text.split())

def calc_characters(text):
	char_counts = {}
	lowered_text = text.lower()
	for char in lowered_text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def print_reports(words_count, chars_dict):
	print("--- Begin report of books/frankenstein.txt ---")
	print(words_count," words found in the document")
	chars_tuples = chars_dict.items()
	sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
	for char,count in sorted_chars:
		if char.isalpha():
			print(f"The '{char}' character was found {count} times")

def main():
	with open("books/frankenstein.txt") as f:
    		file_contents = f.read()
	# print(file_contents)
	num_of_words = calc_words(file_contents)
	num_of_chars = calc_characters(file_contents)
	print_reports(num_of_words, num_of_chars)

main()
