import asyncio

async def async_square(n):
    await asyncio.sleep(0)
    return n * n

"""
|
|
|
"""

async def gather_squares(numbers):
    tasks = [async_square(n) for n in numbers]
    return await asyncio.gather(*tasks)
