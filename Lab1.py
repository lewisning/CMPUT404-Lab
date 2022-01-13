import requests

# 1. Get the request version
print(requests.__version__)

# 2. Get the information of google homepage
homepage = requests.get("https://google.com")
print(homepage.text)

