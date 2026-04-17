# 🐍 Python Job Listings Scraper

A beginner-friendly Python web scraping project that collects job listings from the **Fake Python Jobs** website and saves the extracted data into a CSV file.

## 📌 Project Overview

This scraper fetches job postings from:

https://realpython.github.io/fake-jobs/

It extracts the following information for each job listing:

- Job Title  
- Company Name  
- Location  
- Job Detail URL  

The data is then stored in a CSV file for easy analysis.

---

## 🛠 Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- CSV Module

---

## 📂 Project Structure

```bash
Python-Job-Listings-Scraper/
│── scraper.py
│── jobs.csv
│── README.md
│── .gitignore
│── LICENSE
```
---
## 🚀 How to Run
1. Clone the Repository
   
   ```bash
   git clone https://github.com/amber3905/Python-Job-Listings-Scraper.git
   cd Python-Job-Listings-Scraper
   ```
2. Install Dependencies
   
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the Script
   
   ```bash
   python scraper.py
   ```
---
## 📄 Example Output
|Job Title|Company Name|Location|URL|
|---------|------------|--------|---|
|Python Developer|ABC Corp|New York, NY|https://example.com/job1|
|Data Analyst|XYZ Ltd|Remote|https://example.com/job2|
|Backend Engineer|DevSoft|London, UK|https://example.com/job3|

---
## ✅ Features
- Clean and readable Python code
- Extracts structured job data
- Saves results to CSV
- Handles missing fields
- Beginner-friendly project
---
## 📚 What I Learned
Through this project, I learned:
- How to inspect HTML structure
- How to scrape websites using Python
- How to use BeautifulSoup selectors
- How to save scraped data into CSV
- Basic data extraction workflow
---
## ⚠️ Disclaimer
This project uses a practice website designed for learning web scraping.
No real job listings are collected.

---
## 👨‍💻 Author
Amber-Jo Betts

---
## ⭐ If you found this project helpful, give it a star!
