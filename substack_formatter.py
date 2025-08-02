import sys
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup


def fetch_article(url: str) -> Tuple[str, List[str]]:
    """Download a URL and return its title and paragraph texts."""
    # Disable proxy use by default to avoid corporate proxy issues in some environments
    response = requests.get(url, timeout=10, proxies={"http": None, "https": None})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else url

    article = soup.find("article")
    if article:
        paragraphs = [p.get_text(strip=True) for p in article.find_all("p")]
    else:
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    paragraphs = [p for p in paragraphs if p]
    return title, paragraphs


def format_markdown(title: str, paragraphs: List[str]) -> str:
    body = "\n\n".join(paragraphs)
    return f"# {title}\n\n{body}\n"


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python substack_formatter.py <url> <output_file>")
        return 1
    url, output_path = sys.argv[1], sys.argv[2]
    title, paragraphs = fetch_article(url)
    markdown = format_markdown(title, paragraphs)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)
    print(f"Wrote Substack-ready Markdown to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
