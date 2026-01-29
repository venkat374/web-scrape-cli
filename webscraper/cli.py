import argparse
from .core.utils import normalize_url
from .core.fetch import fetch
from .core.parse import make_soup, get_title, get_links, get_images
import sys

def main():
    parser = argparse.ArgumentParser(description="A simple web scraper (M0)")
    parser.add_argument("url", help="The URL to scrape")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-f", "--fields", nargs="+", choices=["title", "links", "images"], default=["title", "links"], help="Fields to scrape (e.g. title links images)")
    args = parser.parse_args()

    url = normalize_url(args.url)
    # Only print to stdout if not outputting to file (or we can print logs/status to stderr/stdout anyway)
    # user request says "user-friendly", so status updates are good.
    print(f"Scraping content from {url}")

    try:
        resp = fetch(url)
        soup = make_soup(resp.text)
        
        results = {}
        output_lines = []

        if "title" in args.fields:
            title = get_title(soup)
            results["title"] = title
            output_lines.append(f"Page title: {title}")

        if "links" in args.fields:
            links = get_links(soup, url)
            results["links"] = links
            if links:
                output_lines.append("\nAll Links:\n")
                for link in links:
                    output_lines.append(f"-> {link['url']} [{link['text']}]")
            else:
                output_lines.append("No links found.")

        if "images" in args.fields:
            images = get_images(soup, url)
            results["images"] = images
            if images:
                output_lines.append("\nAll Images:\n")
                for img in images:
                    output_lines.append(f"-> {img['src']} [alt: {img['alt']}]")
            else:
                output_lines.append("No images found.")

        final_output = "\n".join(output_lines)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(final_output)
            print(f"Saved output to {args.output}")
        else:
            print(final_output)

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

if __name__ == "__main__":
    main()