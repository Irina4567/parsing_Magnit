import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import aiohttp
import aiofiles
import asyncio
from aiocsv import AsyncWriter


async def collect_data(city_code='2398'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }


    async with aiohttp.ClientSession() as session:

        response = await session.get(url='https://www.wildberries.ru/',
                                     headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')

        print(soup)

    return true


async def main():
    await collect_data(city_code='2398')


if __name__ == '__main__':
    asyncio.run(main())
