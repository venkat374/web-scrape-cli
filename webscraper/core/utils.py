def normalize_url(url):
    """Add https:// if missing."""
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url
