import requests

x = requests.get('https://realpython.github.io/fake-jobs/')

print(x.text)