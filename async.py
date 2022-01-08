import asyncio
import aiohttp
import time

urls = ['https://jsonplaceholder.typicode.com/todos/1']*100000
results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for symbol in urls:
        tasks.append(asyncio.create_task(session.get(symbol)))
    return tasks


async def execute():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
             results.append(await response.json())

asyncio.run(execute())

end = time.time()
total_time = end - start
print("Time taken in {} seconds | Made {} API calls".format(total_time, len(symbols)))
