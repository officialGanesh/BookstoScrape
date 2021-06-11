import requests
import asyncio
from requests_html import HTMLSession
from aiohttp import ClientSession

async def scrape_single_page():
    '''Scraping the first page'''

    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'

    async with ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body




if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(scrape_single_page())
    print('Code Completed 🔥') 