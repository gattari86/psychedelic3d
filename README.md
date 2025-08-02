# psychedelic3d

This repository includes a simple Python script that fetches article content from the web and outputs Substack-ready Markdown.

## Substack formatter

The `substack_formatter.py` script downloads a web page, extracts the title and main paragraphs, and writes a Markdown file you can paste into Substack.

### Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the formatter:
   ```bash
   python substack_formatter.py <url> output.md
   ```

The generated `output.md` contains a Markdown-formatted version of the article.
