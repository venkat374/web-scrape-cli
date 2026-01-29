# WebScraper CLI

A simple **command-line web scraper** built with Python.
This tool fetches a webpage, extracts its title and all links, and displays them neatly in the terminal.

This project was built for learning how CLI tools work and the functionalities were not a pritoritiy during developement.

---

## Features

Fetch any webpage using its URL.

Automatically adds `https://` if you forget it.

## Features

* **Page title**
* **Links**: Extracts all hyperlinks (`<a href="...">`) with text.
* **Images**: Extracts all image sources (`<img src="...">`).
* **Output to File**: Save the results to a file using `-o`.
* **Field Selection**: Choose what to scrape (`title`, `links`, `images`) using `-f`.

---

## Project Structure

```
web-scrape-cli/
│
├── webscraper/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   └── core/
│       ├── __init__.py
│       ├── utils.py        # Helper functions (normalize URL)
│       ├── fetch.py        # Fetch page HTML
│       └── parse.py        # Extract title, links, and images
│
├── pyproject.toml          # Package metadata (for pip install -e .)
└── README.md
```

---

## Installation

1. **Clone the project:**

   ```bash
   git clone https://github.com/venkat374/web-scrape-cli.git
   cd web-scrape-cli
   ```

2. **(Optional but recommended) Create a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies and the package in editable mode:**

   ```bash
   pip install -e .
   ```

---

## ⚙️ Usage

You can run the scraper in **two ways**:

### Option 1 — Using the CLI command (after installation)

```bash
webscraper example.com
```

### Option 2 — Using Python directly

```bash
python -m webscraper.cli example.com
```

### Advanced Usage

**Save output to a file:**
```bash
webscraper example.com -o results.txt
```

**Scrape only specific fields (e.g., images):**
```bash
webscraper example.com -f images
```

**Scrape multiple fields:**
```bash
webscraper example.com -f title links images
```

---

## Example Output

```bash
$ webscraper example.com
Scraping content from https://example.com
Page title: Example Domain

All Links:

-> https://www.iana.org/domains/example [More information...]
```

---

## Notes

* The tool **only scrapes publicly accessible pages**.
* It’s meant for **educational and non-commercial use**.
* Please respect each website’s **robots.txt** and terms of service before scraping.

---

## 🛠️ Future Enhancements (M1 Roadmap)

* [x] Extract images (`--fields images`)
* [ ] Extract meta tags (description, keywords, etc.)
* [x] Save output to file (`--output`)
* [ ] Handle relative links with `urljoin`

---

## 📜 License

MIT License © 2025 venkat374

---
