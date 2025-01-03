import asyncio
from crawl4ai import AsyncWebCrawler

async def fetch_data(url):
    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler(verbose=True) as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(url=url)
        return result.markdown  # Return extracted content as markdown
