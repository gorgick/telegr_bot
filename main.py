from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import Database

bot = Bot('8630054747:AAGCnVlkfExp6AopLEyBP4EuG-SNZJVINXk')
dp = Dispatcher(bot)
db = Database('db.sqlite3')


@dp.message_handler(commands=["start"])
async def cmd_start(message):
    if not db.user_exists(message.from_user.first_name):
        db.add_user(message.from_user.first_name)
    await bot.send_message(message.chat.id, message.from_user.first_name)
    button_1 = InlineKeyboardButton(text="КНОПКА 1", callback_data="button_1_click")
    button_2 = InlineKeyboardButton(text="КНОПКА 2", callback_data="button_2_click")
    button_3 = InlineKeyboardButton(text="КНОПКА 3", callback_data="button_3_click")
    button_4 = InlineKeyboardButton(text="КНОПКА 4", callback_data="button_4_click")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3], [button_4]])
    await message.answer("Choose an option:", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Button 1")
    button_2 = types.KeyboardButton(text="Button 2")
    keyboard.add(button_1, button_2)
    await message.answer(
        "Jerry Falk (Jason Biggs) and David Dobel (Woody Allen), who meet at a business meeting, become fast friends. Their commonality is that they are both fledgling New York City based comedy writers, largely writing material for stand-ups, are Jewish (although David is an atheist), and are each of bundle of different neuroses. Their big difference is that Jerry is twenty-one , while David is sixty, with forty more years worth of life experience, knowledge, and neuroses. While Jerry writes full time - he is also working on a novel - David has kept his day job as a public school teacher just in case.",
        reply_markup=keyboard)


# @dp.message_handler()
# async def info(message):
#     if message.text.lower() == 'hello':
#         await bot.send_message(message.chat.id, message.from_user.first_name)


@dp.message_handler(content_types=['text'])
async def get_text(message):
    text = message.text
    t = db.create_notification(text)
    await bot.send_message(message.chat.id, t)


executor.start_polling(dp, skip_updates=True)
