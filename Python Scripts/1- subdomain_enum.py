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
subdoms = sub_list.splitlines()

for sub in subdoms:
	# Definition of the HTTP URL request.
	sub_domains = f"http://{sub}.{sys.argv[1]}"
	try:
		# HTTP GET request for the defined URL.
		requests.get(sub_domains)
	# Check if the GET Request get back an error (the request URL is not found).
	except requests.ConnectionError:
		pass
	else:
		print("Valid domain: ", sub_domains)
