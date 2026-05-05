import requests
from bs4 import BeautifulSoup
import re
import csv

try:
    x = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
    x.raise_for_status()
except requests.exceptions.HTTPError:
    print("Error: Status code " + str(x.status_code))
    quit()
except requests.exceptions.RequestException:
    print("Error: Couldn't get URL")
    quit()

y = BeautifulSoup(x.content, "html.parser")

z = y.find_all(True, class_="card-content")
if len(z) == 0:
    print("Error: No job cards found")
    quit()

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
