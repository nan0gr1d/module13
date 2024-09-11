#  module_13_1

import asyncio

async def start_strongman(name, power):
    """
    :param name:  имя силача
    :param power:  подъёмная мощность силача
    """
    print(f'Силач {name} начал соревнования.')
    for number_ball in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {number_ball} шар')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Бывалый', 10))
    task2 = asyncio.create_task(start_strongman('Трус', 3))
    task3 = asyncio.create_task(start_strongman('Балбес', 7))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())
