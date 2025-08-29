import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description="A simple web scraping utility")
parser.add_argument("url", help="The URL to scrape")
args = parser.parse_args()

url = args.url
print(f"Scraping content from {url}")

if "http" or "https" not in url:
    url = "https://" + url

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.text
    print(f"page title: {title}")

    links = soup.find_all('a', href=True)

    print("All Links\n")
    for link in links:
        print(f"-> {link['href']} [{link.text}]")    

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the URL {url}")


    #new