#  module_13_4

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    print(data)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    """
    Упрощенный вариант формулы Миффлина-Сан Жеора:
    для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.
    """
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age'])
    await message.answer(f"Рекомендуемая норма калорий:\n - для мужчин: {calories + 5}\n - для женщин: {calories -161}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
