# Google Serper Search

Claude Code skill for web search and image search using Serper API.

## Installation

```bash
npx skills add shuliuzhenhua-sys/google-serper-search
```

## Configuration

Get a free API key from [serper.dev](https://serper.dev) and set the environment variable:

```bash
export SERPER_API_KEY="your_api_key_here"
```

For permanent setup, add to your shell config:

```bash
echo 'export SERPER_API_KEY="your_api_key"' >> ~/.zshrc
source ~/.zshrc
```

## Usage

### Web Search

```bash
python scripts/serper_search.py "search query" web
```

Returns:
- Knowledge graph
- Organic search results
- People Also Ask questions
- Related searches

### Image Search

```bash
python scripts/serper_search.py "search query" images
```

Returns image URLs, thumbnails, dimensions, and source information.

## Example

```bash
# Search for information
python scripts/serper_search.py "Claude AI" web

# Search for images
python scripts/serper_search.py "mountains" images
```

## License

MIT
