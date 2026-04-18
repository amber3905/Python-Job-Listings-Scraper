import requests
from bs4 import BeautifulSoup

x = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
y = BeautifulSoup(x.content, "html.parser")
z = y.find_all(True, class_="card-content")
for job in z:
    title = job.find("h2").get_text(strip=True)
    company = job.find("h3").get_text(strip=True)
    location = job.find("p",class_="location").get_text(strip=True)
    url = 0
    print("Title:", title+ ", Company:", company+ ", Location:", location)