import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Survey import Survey


async def on_startup(_):
    print('Run')


async def on_shutdown(_):
    print('Off')


API_TOKEN = ''
User_Surveys = dict()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def setInLineButStart():
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text="Помощь",
                               callback_data="help")
    ib2 = InlineKeyboardButton(text="Пройти тест",
                               callback_data="test")
    ikb.add(ib1, ib2)
    return ikb


def set_ikb(survey):
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text=survey.answers[survey.NUMBER_QUESTION][1],
                               callback_data="1")
    ib2 = InlineKeyboardButton(text=survey.answers[survey.NUMBER_QUESTION][2],
                               callback_data="2")
    ib3 = InlineKeyboardButton(text=survey.answers[survey.NUMBER_QUESTION][3],
                               callback_data="3")
    ib4 = InlineKeyboardButton(text=survey.answers[survey.NUMBER_QUESTION][4],
                               callback_data="4")
    ikb.add(ib1, ib2, ib3, ib4)
    return ikb


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Привет, это бот который проверит твои знания по английскому языку, а в будущем еще и научит\n"
                           "Используй кнопку помощи, если хочешь узнать что может бот сейчас\n"
                           "Или переходи сразу к тесту и удивись своему уровню!",
                           reply_markup=setInLineButStart())


@dp.message_handler(commands=['test'])
async def send_test(message: types.Message):
    survey = Survey()
    User_Surveys[message.from_user.id] = survey
    await bot.send_message(chat_id=message.chat.id,
                           text=survey.questions[survey.NUMBER_QUESTION],
                           reply_markup=set_ikb(survey))



@dp.callback_query_handler()
async def run_test(callback: types.CallbackQuery):
    survey = User_Surveys[callback.from_user.id]
    answer_text = survey.questions[survey.NUMBER_QUESTION]
    text = answer_text.replace('______', survey.answers[survey.NUMBER_QUESTION][int(callback.data)])
    survey.answersUser[survey.NUMBER_QUESTION] = int(callback.data)
    #TO DO Выделить ответ пользователя
    await bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None)
    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=text)
    if survey.isEndSurvey():
        await bot.send_message(chat_id=callback.from_user.id,
                               text=survey.getLevelUser())
    else:
        survey.NUMBER_QUESTION += 1
        await bot.send_message(chat_id=callback.from_user.id,
                               text=survey.questions[survey.NUMBER_QUESTION],
                               reply_markup=set_ikb(survey))


@dp.callback_query_handler(text="help")
async def run_help(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text="Бот сейчас может задавать вопросы, ответив на которые можно получить уровень английского")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
