# Libraries import.
import requests

# Variables declaration.
# Change from "Target_URL" to your actual target URL (for example https://assets.tryhackme.com/img/THMlogo.png).
url = "Target_URL"
# Actual HTTP GET reuest for the specified file in the URL
r = requests.get(url, allow_redirects = True)
# Saving the file specified file in the URL
open('THMlogo.png', 'wb').write(r.content)