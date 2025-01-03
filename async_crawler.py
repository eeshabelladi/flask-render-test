from playwright.async_api import async_playwright

async def fetch_data(url):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        content = await page.content()
        await browser.close()
        return content

