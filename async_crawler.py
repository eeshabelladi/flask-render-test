import asyncio
from crawl4ai import AsyncWebCrawler

async def fetch_data(url):
    try:
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url=url)
            return result.markdown
    except Exception as e:
        print(f"Error during fetch: {e}")
        raise

