import requests
import sys

wordlist_file = "<path_file>"
sub_list = open(wordlist_file).read()
subdoms = sub_list.splitlines()

for sub in subdoms:
	sub_domains = f"http://{sub}.{sys.argv[1]}"

	try:
		requests.get(sub_domains)
	except requests.ConnectionError:
		pass
	else:
		print("Valid domain: ", sub_domains)