from aiogram import Bot, Dispatcher, executor, types
import logging
import openai
from datetime import datetime

logging.basicConfig(level=logging.INFO)

chat_api = "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"
bot = Bot(token="6083417439:AAHYplWrbkxvC_daQ5StXriZTMCRTN_CzK8")
dp = Dispatcher(bot)


@dp.message_handler()
async def chat_cmd(message: types.Message):
    # arg = message.get_args()
    # if not arg:
    #     await message.reply("Вы не ввели текст для чата")
    #     return
    openai.api_key = chat_api
    model_engine = "text-davinci-003"
    # prompt = f"{arg}"
    prompt = message.text
    completation = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, # получаем три варианта ответа
        stop=None,
        temperature=0.7)

    responses = [choice.text for choice in completation.choices]
    response = "\n\n".join(responses) + f"\n\n"
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
