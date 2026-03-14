from aiogram import Bot, Dispatcher, executor, types

bot = Bot('8630054747:AAGCnVlkfExp6AopLEyBP4EuG-SNZJVINXk')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Button 1")
    button_2 = types.KeyboardButton(text="Button 2")
    keyboard.add(button_1, button_2)
    await message.answer("Choose an option:", reply_markup=keyboard)


@dp.message_handler()
async def info(message):
    if message.text.lower() == 'hello':
        await bot.send_message(message.chat.id, message.from_user.first_name)


executor.start_polling(dp, skip_updates=True)
