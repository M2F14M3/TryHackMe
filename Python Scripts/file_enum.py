import requests
import sys

wordlist_file = "path_file"
sub_list = open(wordlist_file).read()
files = sub_list.splitlines()

for file in files:
	file_enum = f"http://{sys.argv[1]}/{file}.html"
	r = requests.get(file_enum)
	if r.status_code==404:
		pass
	else:
		print("Valid file:" , file_enum)