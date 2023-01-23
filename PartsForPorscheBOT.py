import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mechanics = types.KeyboardButton("🔧механика взаимодействия🔧")
    logistics = types.KeyboardButton(text="🚚логистика🚚")
    order = types.KeyboardButton(text="📋заявка📋")
    info = types.KeyboardButton(text="❓получить консультацию❓", request_contact=True)
    lastorders = types.KeyboardButton(text="Стоимость завершенных заказов других клиентов")
    keyboard.add(mechanics, logistics, order, info, lastorders)
    mess = f'Привет, {message.from_user.first_name}\nЯ бот 🤖 обратной связи с\
 админом канала @PartsForPorsche. Я помогу быстро узнать стоимость доставки 🚚 , покажу цену запчастей 🔧 по\
 завершенным заявкам других заказчиков и помогу сформировать заказ 📋'
    bot.send_message(message.chat.id, mess, reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    bot.send_contact(192964586, message.contact.phone_number, message.contact.first_name)


#@bot.message_handler(commands=['mechanics'])
#def mechanics(message):
 #   kbrm = types.InlineKeyboardMarkup()
  #  kbrm.add(types.InlineKeyboardButton('Перейти к статье', url='https://telegra.ph/Mehanika-vzaimodejstviya-01-19'))
   # bot.send_message(message.chat.id, 'Переходи по ссылке ниже ⬇️', reply_markup=kbrm, parse_mode='html')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == '🔧механика взаимодействия🔧':
        kbrm = types.InlineKeyboardMarkup()
        kbrm.add(types.InlineKeyboardButton('Перейти к статье',
                                            url='https://telegra.ph/Mehanika-vzaimodejstviya-01-19'))
        bot.send_message(message.chat.id, 'Чтобы прочитать о том, как строится работа, переходи по ссылке ниже ⬇️',
                         reply_markup=kbrm, parse_mode='html')
    elif message.text.strip() == '🚚логистика🚚':
        kbrl = types.InlineKeyboardMarkup()
        kbrl.add(types.InlineKeyboardButton('Перейти к статье о логистике', url='https://telegra.ph/Logistika-01-19'))
        bot.send_message(message.chat.id, 'Чтобы узнать сроки и стоимость логистики переходи по ссылке ниже ⬇️',
                         reply_markup=kbrl, parse_mode='html')
    elif message.text.strip() == '📋заявка📋':
        bot.send_message(message.chat.id, 'Напиши в чат @a_lexe', parse_mode='html')
    elif message.text.strip() == 'Стоимость завершенных заказов других клиентов':
        keyboardlast = types.InlineKeyboardMarkup(row_width=2)
        linkPorsche = types.InlineKeyboardButton('Список Porsche',
                                                 url='https://telegra.ph/Predydushchie-zakazy-01-21')
        linkMercedes = types.InlineKeyboardButton('Список Mersedes',
                                                  url='https://telegra.ph/Predydushchie-zakazy-Mercedes-01-21')
        linkAudi = types.InlineKeyboardButton('Список Audi',
                                              url='https://telegra.ph/Predydushchie-zakazy-Audi-01-21')
        linkLambo = types.InlineKeyboardButton('Список Lamborghini',
                                               url='https://telegra.ph/Predydushchie-zakazy-Lamborghini-01-21')
        keyboardlast.add(linkPorsche, linkMercedes, linkAudi, linkLambo)
        bot.send_message(message.chat.id, 'Вибери интересующую марку автомобиля ⬇️', reply_markup=keyboardlast, parse_mode='html')
    else:
        answer = 'Ничего не понял, но очень интересно!'
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
