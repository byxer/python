import requests
import datetime
from config import bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("В каком городе Вы хотите узнать сводку погоды?")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        await message.reply(f"На {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\nПогода в городе: {city}\nТемпература: {cur_weather}C\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/c\nВосход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}")
    except:
        await message.reply("Проверте название города")

if __name__ == "__main__":
    executor.start_polling(dp)