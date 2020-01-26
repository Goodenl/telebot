import telebot
import config
import parser
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def stiker_Hi(message):
	sti = open('stickers/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Рэндоме')
	item2 = types.KeyboardButton('Як справи, хлопче?')
	item3 = types.KeyboardButton('Слитая инфаа!')

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, 'Добро пожаловать, мистер {0.first_name} {0.last_name}!\nЯ - <b>{1.first_name}</b>, бот для теста и проверки фотографий.'.format(message.from_user, bot.get_me()),
		parse_mode = 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def pressMarkup(message):
	if message.chat.type == 'private':
		if message.text == 'Рэндоме':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == 'Як справи, хлопче?':

			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data="good")
			item2 = types.InlineKeyboardButton("Чёт умерать пора!", callback_data="bad")

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Добре! Як сам?', reply_markup=markup)
		elif message.text == 'Слитая инфаа!':
			bot.send_message(message.chat.id, parser.title)
		else:
			bot.send_message(message.chat.id, 'Я ничего не понял(')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				#snd = open('/temp/nicedo.webp', 'rb')
				#bot.send_sticker(chat_id=call.message.chat.id, sticker=snd)
				bot.send_message(chat_id=call.message.chat.id, text='Прекрасно!')
			elif call.data == 'bad':
				#sbd = open('/temp/baddo.webp', 'rb')
				#bot.send_sticker(chat_id=call.message.chat.id, sticker=sbd)
				bot.send_message(chat_id=call.message.chat.id, text='Эт\' плохо.')

			#remove inline keyboard
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Як справи, хлопче?",
				reply_markup=None)

			#show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="Push Alert!!!")

	except Exception as e:
		print(repr(e))

# run 
bot.polling(none_stop=True)