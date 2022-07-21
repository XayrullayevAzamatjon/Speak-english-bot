# Creator Azamatjon Xayrullayev
import logging
from aiogram import Bot, Dispatcher, executor, types
from oxford import getDefinition
from googletrans import Translator

transtlator = Translator()

API_TOKEN = 'Bot Token Here '

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher3.1.0a0
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Translator bot and Oxford dictionary!\nCreator{name}.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Botni ishga tushurish uchun so`z(en/uz) yoki 2 va undan ortiq so`zdan iborat gap  yuboring")


@dp.message_handler()
async def translate(message: types.Message):
    lang = transtlator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = "uz" if lang == "en" else 'en'
        await message.reply(transtlator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = transtlator.translate(message.text, dest='en').text
        lookup = getDefinition(word_id)
        if lookup:
            await message.reply(f"Word:{word_id}\nDefinitions:\n{lookup['definitions']}")
            if lookup.get("audio"):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so`z topilmadi ! Qaytadan urinib ko`ring ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
