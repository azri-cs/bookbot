from stats import calc_words, get_list_of_dictionaries
import sys

def print_help():
	print("Usage: python3 main.py <path_to_book>")

def print_reports(file_contents, file_path):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print("Found", calc_words(file_contents), "total words")
	print("--------- Character Count -------")
	sorted_chars = get_list_of_dictionaries(file_contents)

	for char,count in sorted_chars:
		if char.isalpha():
			print(f"{char}: {count}")

	print("============= END ===============")

def main():
	if len(sys.argv) == 1:
		print_help()
		sys.exit(1)
	else:
		file_path = sys.argv[1]
		with open(file_path) as f:
    			file_contents = f.read()
		print_reports(file_contents, file_path)

main()
