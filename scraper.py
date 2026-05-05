import requests
from bs4 import BeautifulSoup
import re
import csv

# Step 1: Fetch the webpage
try:
    response = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("Error: Status code " + str(response.status_code))
    quit()
except requests.exceptions.RequestException:
    print("Error: Couldn't get URL")
    quit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all job cards
job_cards = soup.find_all(True, class_="card-content")

# Handle case where no jobs are found
if len(job_cards) == 0:
    print("Error: No job cards found")
    quit()

# Step 4: Write data to CSV file
with open("jobs.csv", "w") as file:
    writer = csv.writer(file)

    # Write header row
    headers = ["Title", "Company", "Location", "URL"]
    writer.writerow(headers)

    # Step 5: Extract data from each job card
    for job in job_cards:
        title_element = job.find("h2")
        company_element = job.find("h3")
        location_element = job.find("p",class_="location")
        link_element = job.find("a", href=re.compile("jobs"))

        # Validate that all required elements exist
        if (
            title_element is not None and
            company_element is not None and
            location_element is not None and
            link_element is not None
        ):
            # Extract text safely
            title = title_element.get_text(strip=True)
            company = company_element.get_text(strip=True)
            location = location_element.get_text(strip=True)
            url = link_element.get("href")

            # Write row to CSV
            row = [title, company, location, url]
            writer.writerow(row)
