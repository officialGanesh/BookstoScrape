import os
import csv
import asyncio
from requests_html import HTML
from aiohttp import ClientSession

async def scrape_single_page():
    '''Scraping the first page'''

    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'

    async with ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()

            html_body = await response.read()

            # Saving the html as index.html
            with open('Output\SingleScrape\index.html','w') as f:
                source = f.write(html_body.decode())

            tasks = []
            tasks.append(
                asyncio.create_task(
                    scrape_single_csv()
                )
            )
            page_content = asyncio.gather(*tasks)
            

async def scrape_single_csv():
    '''Scraping and writing the data in csv'''
    with open('Output\SingleScrape\index.html','r') as f:
        source = f.read()
        html = HTML(html=source)

        csv_file = open('Output\SingleScrape\data.csv','w',newline='')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title','Image','Price'])      

        containers =  html.find('.col-xs-6')

        for container in containers:

            try:
                title =  container.find('h3',first=True).text

                img_link =  container.find('img',first=True).attrs['src'].split('../../../')[1]
                img = os.path.join(f'http://books.toscrape.com/{img_link}')

                price =  container.find('p.price_color',first=True).text

                
            except Exception as e:
                print('Something Went Wrong ',e)

            csv_writer.writerow([title,img,price])
        csv_file.close()
        

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(scrape_single_page())
    print('Code Completed 🔥') 