import requests
from bs4 import BeautifulSoup

x = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
y = BeautifulSoup(x.content, "html.parser")
z = y.find_all(True, class_="card-content")

print(z)