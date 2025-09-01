from bs4 import BeautifulSoup
from .utils import normalize_url

def make_soup(html):
    return BeautifulSoup(html, "html.parser")

def get_title(soup):
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "(no title)"

def get_links(soup, base_url):
    links = []
    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True) or "[no text]"
        href = a["href"]
        links.append({"url": href, "text": text})
    return links
