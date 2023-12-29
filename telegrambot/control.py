import telebot
from telebot.types import Message
import os
import random
from telebot import types
BOT_TOKEN = '6944912046:AAFw_6lmdlDG5lbr3vhLzyppzXbfcKf60xM'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg:Message):
    bot.send_message(msg.chat.id, 'Assalomu alaykum Islom Karimov sotuv botiga hush kelibsiz !!!')


points = 0

words1 = ["To'gri🖐️", 'Boladi ', 'Shunday keting', 'Yahshiga oxshavoti']
random1 = random.choices(words1)
random2 = random1[0] or random1[1] or random1[2] or random1[3]

words2 = ["Notori", 'Yomon !', 'Savolni tushundizmi ozi ?', 'Oqimaganligingiz shu yerdan malum ']
random1_ = random.choices(words2)
random2_ = random1_[0] or random1_[1] or random1_[2] or random1_[3]



@bot.message_handler(content_types=['text'])
def math_quiz(message):
    global points
    global random2
    global random2_
    if message.text == '/Quiz' or message.text == '/quiz':
        points = 0

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('72')
        item2 = types.KeyboardButton('80')
        item3 = types.KeyboardButton('74')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '1) 8 * 9 = ?', reply_markup=markup)

    if message.chat.type == 'private':
        # 1-savol
        if message.text == '72':
            bot.send_message(message.chat.id, random2)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('90')
            item2 = types.KeyboardButton('1515')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) 6 * 15 = ?', reply_markup=markup)

        elif message.text == '80':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 72')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('90')
            item2 = types.KeyboardButton('115')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) 6 * 15 = ?', reply_markup=markup)

        elif message.text == '74':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 72')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('90')
            item2 = types.KeyboardButton('115')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '2) 6 * 15 = ?', reply_markup=markup)

        # 2-savol
        if message.text == '90':
            bot.send_message(message.chat.id, random2)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('75')
            item2 = types.KeyboardButton('115')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '3) 15 * 5 = ?', reply_markup=markup)

        elif message.text == '115':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 90')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('75')
            item2 = types.KeyboardButton('115')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '3) 15 * 5 = ?', reply_markup=markup)

        elif message.text == '50':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 225')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('75')
            item2 = types.KeyboardButton('115')
            item3 = types.KeyboardButton('50')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '3) 15 * 5 = ?', reply_markup=markup)

        # 3-savol
        if message.text == '75':
            bot.send_message(message.chat.id, random2)
            points += 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('8585')
            item2 = types.KeyboardButton('7205')
            item3 = types.KeyboardButton('7225')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '4) 85 * 85 = ?', reply_markup=markup)

        elif message.text == '115':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 75')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('8585')
            item2 = types.KeyboardButton('7205')
            item3 = types.KeyboardButton('7225')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '4) 85 * 85 = ?', reply_markup=markup)

        elif message.text == '50':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 75')
            points += 0

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('8585')
            item2 = types.KeyboardButton('7205')
            item3 = types.KeyboardButton('7225')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, '4) 85 * 85 = ?', reply_markup=markup)


        # 10 -savol
        if message.text == '7225':
            bot.send_message(message.chat.id, random2)
            points += 1

        elif message.text == '8585':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 7225')
            points += 0

        elif message.text == '7205':
            bot.send_message(message.chat.id, random2_)
            bot.send_message(message.chat.id, 'Javob: 7225')
            points += 0
        bot.send_message(message.chat.id, f"Sizning balingiz: {points}")


bot.polling()
bot.infinity_polling()