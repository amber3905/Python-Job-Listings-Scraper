import requests
from bs4 import BeautifulSoup

x = requests.get("https://realpython.github.io/fake-jobs/")
y = BeautifulSoup(x.content, "html.parser")

print(y.prettify())