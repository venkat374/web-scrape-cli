import argparse
from .core.utils import normalize_url
from .core.fetch import fetch
from .core.parse import make_soup, get_title, get_links

def main():
    parser = argparse.ArgumentParser(description="A simple web scraper (M0)")
    parser.add_argument("url", help="The URL to scrape")
    args = parser.parse_args()

    url = normalize_url(args.url)
    print(f"Scraping content from {url}")

    try:
        resp = fetch(url)
        soup = make_soup(resp.text)

        title = get_title(soup)
        print(f"Page title: {title}")

        links = get_links(soup, url)
        if links:
            print("\nAll Links:\n")
            for link in links:
                print(f"-> {link['url']} [{link['text']}]")
        else:
            print("No links found.")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
