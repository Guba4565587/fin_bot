import asyncio
import logging
import sys
#import gspread
from os import getenv


from aiogram import Bot, Dispatcher, html, F, Router
from aiogram.fsm.context import FSMContext 
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

# Bot token can be obtained via https://t.me/BotFather
#bot = Bot(token='7895456806:AAH29dJRrnyMyB61YkQeJ6VXAiPP8fT2TwI', session=session)
TOKEN = os.environ.get("TOKEN")

class User_Info(StatesGroup):
    fio = State()
    mi_number = State()
    fio_client = State()
    cart_cl = State()
    #название переменной 
    #пример 

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
user_info = Router()
button1 = KeyboardButton(text="/T_BANK")
button2 = KeyboardButton(text="/VTB")
button3 = KeyboardButton(text="список всех команд")
button4 = KeyboardButton(text="/MTC")
button5 = KeyboardButton(text="/GASPROM")
button6 = KeyboardButton(text="/отправить")
button7 = KeyboardButton(text="/T_PREMIYM")
button8 = KeyboardButton(text="/Изменить")
kpack = ReplyKeyboardMarkup(keyboard=[[button1,button2,button4,button5,button7]],resize_keyboard=True)
kpack_2 = ReplyKeyboardMarkup(keyboard=[[button6,button8]],resize_keyboard=True)
kpack_T = ReplyKeyboardMarkup(keyboard=[[button7]],resize_keyboard=True)


button1_P = KeyboardButton(text="T_BANK")
button2_P = KeyboardButton(text="VTB")
button3_P = KeyboardButton(text="список всех команд")
button4_P = KeyboardButton(text="MTC")
button5_P = KeyboardButton(text="GASPROM")
button6_P = KeyboardButton(text="отправить")
button7_P = KeyboardButton(text="T_PREMIYM")
kpack_p = ReplyKeyboardMarkup(keyboard=[[button1_P,button2_P,button4_P,button5_P,button7_P]],resize_keyboard=True)
kpack_T_P = ReplyKeyboardMarkup(keyboard=[[button7]],resize_keyboard=True)
#gc = gspread.service_account() 
#sh = gc.open_by_key("1nP6A9PI-T6lNbsuR_fKOK4zk0p4O5LgpXdHNOlMmRsY")

##@dp.message(Command("reada1")) 
#async def read_handler(message : Message) -> any: 
    #result = sh.sheet1.get('A1') 
    #await message.answer(str(result)) 

#@dp.message(Command("writeb2")) 
#async def read_handler(message : Message) -> any: 
    #sh.sheet1.update_acell('B2', "abcd") 
    #await message.answer("success?")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   await message.answer(f"приветствуем тебя, {html.bold(message.from_user.full_name)}!" "Приветствуем вас,на связи ReferHub" "\n Мы рады видеть вас в нашей команде! Наша команда стремится создать уникальные возможности для заработка и взаимовыгодного сотрудничества." "\n список всех команд - (/Command)")

@dp.message(Command("Command"))
async def echo_handler(message: Message) -> None:
    await message.answer("(/fill_sale)-!!!Здесь продажу фиксировать будешь" "\n (/get_a_link) - !!!Здесь QR на карту найдешь!!!" " \n(/info) - !!!Здесь важное прочитаешь!!!" )  

@dp.message(Command("get_a_link"))
async def echo_handler(message: Message) -> None:
    await message.answer("какой банк ?",reply_markup=kpack)
    await message.answer(reply_markup=kpack_T) 


@dp.message(Command("get_script"))
async def echo_handler(message: Message) -> None:
    await message.answer("СКРИПТРаботник: Здравствуйте! Как ваше настроение сегодня?Незнакомец: Здравствуйте. Что вам нужно?Работник: Я представляю [название компании/банка], и у нас есть уникальное предложение по карте, которое может вас заинтересовать.Незнакомец: Мне не интересно. У меня уже есть карта.Работник: Понимаю, но у нас действительно выгодные условия, например, кэшбэк на покупки и бесплатное обслуживание в первый год. Это может помочь вам сэкономить.Незнакомец: Кэшбэк? И что? Я не собираюсь тратить время на это.Работник: Я вас понимаю, но представьте, если вы получите 5% кэшбэка на все ваши покупки. Это может быть значительная сумма в конце года. Например, если вы тратите 30 000 рублей в месяц, вы можете вернуть 1 800 рублей в конце месяца, а я уверен , что выши траты больше.Незнакомец: Ну, возможно... Но я не уверен, что это стоит усилий.Работник: На самом деле, оформление карты занимает всего 10 минут, и с ней вы также получите доступ к эксклюзивным предложениям и скидкам от наших партнеров. Это может быть удобно!Незнакомец: Звучит неплохо, но мне все равно не хватает времени.Работник:И если вам не понравится, вы всегда сможете отменить карту. Это абсолютно безрисковое предложение!Незнакомец: Ладно, давайте попробуем. Заполню анкету.Работник: Отлично! Я помогу вам с оформлением. Спасибо за ваше время!")


@dp.message(Command("info"))
async def echo_handler(message: Message) -> None:
    await message.answer("Все что вам понадобится!!! \n‼️ЗАРПЛАТА‼️ \nДеньги за любую продажу приходят за 25-35 дней , оплата приходит неделями, то есть если вы работаете с 1-7 февраля, деньги за эту неделю придут  в первую неделю марта. \n‼️ГДЕ РАБОТАТЬ?‼️ \nРаботаем везде.\n‼️Oформить карту можно всем с 14 лет‼️Это значит, что можно оформлять как и своих знакомых , так и просто прохожих, посетителей ТЦ и так далее.\n Как работать?Если это смена, где вы ходите по людным местам и совершаете продажи, вы должны написать в чат, что вы на смене и указать место работы, после подтверждения свешера, выходите и начинаете работать, заходите в бот, выбираете карту которую будете оформлять, ВНИМАТЕЛЬНО все читаете и начинаете работать,жедаем удачи.Если вы оформляете своих знакомых, родственников, друзей, то заходите в бот, выбираете карту которую будете оформлять, ВНИМАТЕЛЬНО все читаетеи начинаете работать,жедаем удачи.Что говорить когда подходишь к людям? Главное понимать когда человек неполностью не готов, с такого человека вы ничего не получите, так же люди которые чем то заняты , например едят или работают на фуд-корте за ноутбуком, тоже ничего не оформят , далее будет скрипт разговора , модифицируете его , пробуйте разные варианты и у вас все получится" " \n ✔️ /get_script - как подходить к людям ✔️" )
    #сделай ссылку на скрипт 



@dp.message(Command("T_BANK"))
async def echo_handler(message: Message) -> None:
    await message.answer("https://trk.ppdu.ru/click?uid=213074&pid=2&oid=bf70e909-3ec2-4ddc-ac26-4e2c15d03bb3&erid=Kra23oUWc" "\n • Целевое действие: Дебетовая карта - выдача + POS-транзакция на любую сумму!!!\nАкция: при оформление карты 3 месяца T-Premium бесплатно\nЗП с одной крты:400₽",reply_markup=ReplyKeyboardRemove())

@dp.message(Command("VTB"))
async def echo_handler(message: Message) -> None:
    await message.answer("https://trk.ppdu.ru/click/9OaxiKf0?erid=Kra23bfT9" "\n Целевое действие: Встреча с представителем + Покупка дороже 100₽ новым клиентом!!!\nЗП с одной крты:400₽",reply_markup=ReplyKeyboardRemove())

@dp.message(Command("MTC"))
async def echo_handler(message: Message) -> None:
    await message.answer("https://trk.ppdu.ru/click/KuCEbLRq?erid=2SDnjcxTaXt" "\n Целевое действие: Встреча с представителем + Покупка дороже 100₽ новым клиентом!!!\nАкция:Повышеный кэшбек и плюшки для пользователей МТС\nЗП с одной крты:400₽",reply_markup=ReplyKeyboardRemove())

@dp.message(Command("GASPROM"))
async def echo_handler(message: Message) -> None:
    await message.answer("https://trk.ppdu.ru/click/tX5jniNx?erid=Kra23uRPu" "\n Целевое действие: Встреча с представителем + Покупка дороже 100₽ новым клиентом!!!\nАкция:Это карта премиум клиента, то есть повышеный кэшбек и бесплатное обслежевание\n ЗП с одной крты:600₽",reply_markup=ReplyKeyboardRemove())


@dp.message(Command("T_PREMIYM"))
async def echo_handler(message: Message) -> None:
    await message.answer("https://trk.ppdu.ru/click/fgxah9m9?erid=Kra245bYt" "\n Целевое действие: Встреча с представителем + Покупка дороже 100₽ новым клиентом!!!\nАкция:Это карта премиум клиента, то есть металическая карта, повышеный кэшбек и бесплатное обслужевание\n ЗП с одной крты:400₽",reply_markup=ReplyKeyboardRemove())


@dp.message(Command("fill_sale"))  
async def ответ (message: Message, state: FSMContext) -> None:
    await state.set_state(User_Info.fio)
    await message.answer("твой фио ?",reply_markup=ReplyKeyboardRemove())
     #= вопрос х


@user_info.message(User_Info.fio)
async def fio(message: Message, state: FSMContext) -> None:
#ответ на вопрос х (fio)
    await state.update_data(fio = message.text)
    await state.set_state(User_Info.mi_number)
    await message.answer("твой номер телефона ?")


@user_info.message(User_Info.mi_number)
async def mi_number(message: Message, state: FSMContext) -> None:
    await state.update_data(mi_number = message.text)
    await state.set_state(User_Info.fio_client)
    await message.answer("фио клиента ?")


@user_info.message(User_Info.fio_client)
async def fio_client (message: Message, state: FSMContext) -> None:
    await state.update_data(fio_client = message.text)
    await state.set_state(User_Info.cart_cl)
    await message.answer("какую карту оформил?",reply_markup=kpack_p)

@user_info.message(User_Info.cart_cl)
async def cart_cl (message: Message, state: FSMContext) -> None:
    #await state.update_data(cart_cl = message.text)
    data =    await state.update_data(cart_cl = message.text) 
    #data-это переменная 
    a = data.get("fio")
    b = data.get("mi_number")
    c = data.get("fio_client")
    d = data.get("cart_cl")
    await message.answer(
        f"Отчёт:\n"
        f"ФИО : {a}\n"
        f"НОМЕР ТЕФОНА: {b}\n"
        f"ФИО КЛИЕНТА: {c} \n"
        f"КАРТУ КОТОРУЮ ОФОРМИЛ:\n{d}",
        reply_markup=kpack_2
    )
    #await message.answer(reply_markup=kpack_2)
    #await message.answer("отчёт:" + str(a) + str(b) + str(c),reply_markup=kpack_2)
    await message.answer("⚠️проверь всё ли правильно заполнил⚠️,\n✅ Скопируй это сообщение и отправь нам в @ref_bro✅")
    


@dp.message(Command("отправить"))  
async def echo_handler (message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("✅ Скопируй это сообщение и отправь нам в @ref_bro✅",reply_markup=ReplyKeyboardRemove())
@dp.message(Command("Изменить"))
async def ответ_2 (message: Message, state: FSMContext) -> None:
    await state.clear()
    await ответ(message,state)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(user_info)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
