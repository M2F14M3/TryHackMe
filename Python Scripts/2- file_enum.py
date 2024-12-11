# Libraries import.
import requests
import sys

# Variables declaration.
# Change from "path_file" to the actual path of the wordlist file.
wordlist_file = "path_file"
# Opening of the wordlist file in reading mode.
sub_list = open(wordlist_file).read()
# Assing all the content of the wordlist file to an array.
# One cell per each line.
files = sub_list.splitlines()

for file in files:
	# Definition of the HTTP URL request.
	file_enum = f"http://{sys.argv[1]}/{file}.html"
	# HTTP GET request for the defined URL.
	r = requests.get(file_enum)
	# Check if the GET Request get back a 404 status code (not found).
	if r.status_code==404:
		pass
	else:
		print("Valid file:" , file_enum)
