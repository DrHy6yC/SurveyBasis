import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from Survey import Survey
from User import User
from SQL_BOT import SQL_BOT


async def on_startup(_):
    print('Run')


async def on_shutdown(_):
    print('Off')


User_Surveys = dict()
Users = dict()
User_Answers = dict()
IS_SURVEY_ON = False

logging.basicConfig(level=logging.INFO)


sql_bot = SQL_BOT()

API_TOKEN = sql_bot.SELECT_TABLE("CONSTANTS", {"CONSTANT_ID": 1})[0][2]
MY_ID = sql_bot.SELECT_TABLE("CONSTANTS", {"CONSTANT_ID": 2})[0][2]

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def setButStart():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text="Помощь")
    b2 = KeyboardButton(text="Пройти тест")
    b3 = KeyboardButton(text="START")
    kb.add(b3, b1, b2)
    return kb


def set_ikb_survey(survey):
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


@dp.message_handler(commands='level')
async def send_level(message: types.Message):
    try:
        if sql_bot.get_ONE_USER(message.from_user.id):
            level = sql_bot.get_ONE_USER(message.from_user.id)[2]
            dict_where = {"LEVEL_ID": level}
            text_level = sql_bot.SELECT_TABLE("LEVELS", dict_where)
            text_level_send = f"Сейчас твой уровень: {text_level[0][1]}"
            await message.answer(text=text_level_send)
        else:
            await message.answer(text="У тебя нет уровня, пройди тест: /test")
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await message.answer(text="Что-то пошло не так, попробуй ещё раз.")


@dp.message_handler(filters.Text(equals="START"))
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        user = User()
        user_bd = sql_bot.get_ONE_USER(message.from_user.id)
        if user_bd:
            user.USER_ID = user_bd[0]
            user.USER_FULL_NAME = user_bd[1]
            user.USER_LEVEL = user_bd[2]
            user.USER_ACCESS = user_bd[3]
            user.USER_LOGIN = user_bd[4]

        else:
            dict_insert = {"USER_FULL_NAME":  message.from_user.full_name,
                           "USER_LEVEL": 3,
                           "USER_ACCESS": 0,
                           "USER_LOGIN": str(message.from_user.id)}
            sql_bot.INSERT_TABLE("USERS", dict_insert)
            sql_bot.SELECT_TABLE("USERS")
        Users[user.USER_ID] = user
        text_hi = """ Привет, это бот который проверит твои знания по английскому языку, а в будущем еще и научит.\n
        Используй кнопку помощи, если хочешь узнать что может бот сейчас.\n
        Или переходи сразу к тесту и удивись своему уровню!"""
        await bot.send_message(chat_id=message.chat.id,
                               text=text_hi,
                               reply_markup=setButStart())
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await message.answer(text="Что-то пошло не так, попробуй ещё раз.")


#TODO Отрефакторить
@dp.message_handler(filters.Text(equals="Пройти тест"))
@dp.message_handler(commands=['test'])
async def call_test_message(message: types.Message):
    try:
        if message.from_user.id in User_Surveys:
            text_error = "Уже запущен один опрос, второй можно запустить когда пройдешь этот"
            await message.answer(text=text_error)
        else:
            survey = Survey()
            id_user = message.from_user.id
            User_Surveys[id_user] = survey
            text_Question = survey.questions[survey.NUMBER_QUESTION]
            await bot.send_message(chat_id=message.chat.id,
                                   text=text_Question,
                                   reply_markup=set_ikb_survey(survey))
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await message.answer(text="Что-то пошло не так, попробуй ещё раз.")


@dp.callback_query_handler(text="1")
@dp.callback_query_handler(text="2")
@dp.callback_query_handler(text="3")
@dp.callback_query_handler(text="4")
#TODO Сделать так что бы другие пользователи не могли пройти уже начатый тест
async def run_test(callback: types.CallbackQuery):
    try:
        id_user = callback.from_user.id
        id_chat = callback.message.chat.id
        survey = User_Surveys[id_user]
        answer_text = survey.questions[survey.NUMBER_QUESTION]
        answer_user = survey.answers[survey.NUMBER_QUESTION][int(callback.data)]
        question_insert_answer = answer_text.replace('______', f'<u><em>{answer_user}</em></u>')
        survey.answersUser[survey.NUMBER_QUESTION] = int(callback.data)
        await bot.edit_message_reply_markup(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            reply_markup=None)
        await bot.edit_message_text(
            chat_id=id_chat,
            message_id=callback.message.message_id,
            parse_mode="html",
            text=question_insert_answer)
        if survey.isEndSurvey():
            text_level_user = survey.getLevelUser()
            dict_where = {"LEVEL_NAME": text_level_user}
            id_level = sql_bot.SELECT_TABLE("LEVELS", dict_where)
            dict_atr = {"USER_LEVEL": id_level[0][0]}
            dict_where = {"USER_LOGIN": id_user}
            sql_bot.UPDATE_TABLE("USERS", dict_atr, dict_where)
            sql_bot.get_ONE_USER(id_user)
            dict_atr = {"USER_ID": sql_bot.get_ONE_USER(id_user)[0],
                        "ANSWER": survey.answersUser}
            sql_bot.INSERT_TABLE("ANSWERS", dict_atr)
            text_user_end = f"Твой уровень: {text_level_user}!"
            await bot.send_message(chat_id=id_chat,
                                   text=text_user_end)
            User_Surveys.pop(id_user, None)
        else:
            survey.NUMBER_QUESTION += 1
            text_next_question = survey.questions[survey.NUMBER_QUESTION]
            await bot.send_message(chat_id=id_chat, #id_user,
                                   text=text_next_question,
                                   reply_markup=set_ikb_survey(survey))
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await bot.send_message(chat_id=callback.from_user.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


#@dp.callback_query_handler(text="help")
@dp.message_handler(filters.Text(equals="Помощь"))
@dp.message_handler(commands='help')
async def run_help(message: types.message):
    try:
        print(type(message))
        text_help = "Бот сейчас может задавать вопросы, ответив на которые можно получить уровень английского"
        await bot.send_message(chat_id=message.chat.id,
                               text=text_help)
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await bot.send_message(chat_id=message.chat.id,
                               text="Что-то пошло не так, попробуй ещё раз.")


@dp.message_handler(filters.Text(equals="error"))
@dp.message_handler(filters.Text(equals="Вызвать ошибку"))
@dp.message_handler(filters.Text(equals="Делаю больно"))
async def error_func(message: types.Message):
    try:
        await bot.send_message("rferfer")
    except Exception as error:
        await bot.send_message(chat_id=MY_ID,
                               text=f"Ошибка в боте:{error}")
        await bot.send_message(chat_id=message.from_user.id,
                               text="Что-то мне поплохело")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    sql_bot.end_con()
