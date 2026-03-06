from aiogram import Bot, Dispatcher, executor, types

bot = Bot('8630054747:AAGCnVlkfExp6AopLEyBP4EuG-SNZJVINXk')
dp = Dispatcher(bot)


@dp.message_handler()
async def info(message):
    if message.text.lower() == 'hello':
        await bot.send_message(message.chat.id, message.from_user.first_name)


executor.start_polling(dp, skip_updates=True)
