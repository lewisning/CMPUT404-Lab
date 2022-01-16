import requests

# 1. Get the request version
print(requests.__version__)

# 2. Get the information of google homepage
homePage = requests.get("https://google.com")
print(homePage.text)

# 3. Download itself from GitHub and print out the content
itself = requests.get("https://raw.githubusercontent.com/lewisning/CMPUT404-Lab/main/Lab1.py")
print(itself.text)