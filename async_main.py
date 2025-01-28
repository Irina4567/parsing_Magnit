import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import aiohttp
import aiofiles
import asyncio
from aiocsv import AsyncWriter
import requests


async def collect_data(city_code='2398'):
    # URL API WB
    url = "https://catalog.wb.ru/catalog/pants/v2/catalog"

    # Параметры запроса
    params = {
        "ab_testing": "false",
        "appType": "1",
        "cat": "8127",
        "curr": "rub",
        "dest": "123589442",
        "hide_dtype": "10",
        "lang": "ru",
        "page": "1",
        "sort": "popular",
        "spp": "30",
        "xsubject": "147",
    }

    try:
        # Отправка GET-запроса
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP

        # Парсинг ответа в формате JSON
        data = response.json()
        print(data)  # Вывод результата
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")

    return 'NO'


async def main():
    await collect_data(city_code='2398')


if __name__ == '__main__':
    asyncio.run(main())
