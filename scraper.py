import requests

# Make a request to the web page
x = requests.get("https://realpython.github.io/fake-jobs/")

# Print the response text
print(x.text)