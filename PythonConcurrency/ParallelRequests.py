import aiohttp
import asyncio

URLS = [
    "http://www.laughfactory.com/jokes/clean-jokes/2",
    "http://www.laughfactory.com/jokes/clean-jokes/3",
    "http://www.laughfactory.com/jokes/clean-jokes/4",
    "http://www.laughfactory.com/jokes/clean-jokes/5",
    "http://www.laughfactory.com/jokes/clean-jokes/6",
    "http://www.laughfactory.com/jokes/clean-jokes/7",
    "http://www.laughfactory.com/jokes/clean-jokes/8",
    "http://www.laughfactory.com/jokes/clean-jokes/9",
    "http://www.laughfactory.com/jokes/clean-jokes/10",
    "http://www.laughfactory.com/jokes/clean-jokes/11",
    "http://www.laughfactory.com/jokes/clean-jokes/12",
    "http://www.laughfactory.com/jokes/clean-jokes/13",
]

async def get_url(url, session):
    async with session.get(url = url) as resp:
        print("Got {url} - {code}".format(
            url = url,
            code = resp.status
        ))
        assert resp.status == 200
        return await resp.text()

async def main():
    connector = aiohttp.TCPConnector(limit=4)
    async with aiohttp.ClientSession(connector=connector) as session:
        results = await asyncio.gather(*[
            get_url(url, session) for url in URLS
        ])
        return results


loop = asyncio.new_event_loop()
x = loop.run_until_complete(main())