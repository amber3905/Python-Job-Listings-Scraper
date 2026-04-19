import requests
from bs4 import BeautifulSoup
import re
import csv

x = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
y = BeautifulSoup(x.content, "html.parser")
z = y.find_all(True, class_="card-content")
with open("jobs.csv", "w") as f:
    fWriter = csv.writer(f)
    fields = ["Title", "Company", "Location", "URL"]
    fWriter.writerow(fields)
    for job in z:
        title = job.find("h2").get_text(strip=True)
        company = job.find("h3").get_text(strip=True)
        location = job.find("p",class_="location").get_text(strip=True)
        url = job.find("a", href=re.compile("jobs"))
        row = [title,company,location,url.get("href")]
        fWriter.writerow(row)
