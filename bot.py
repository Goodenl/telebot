import telebot
import config
import parser
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

project = ['World-and-excellence','polskapizda','telegram channel']

@bot.message_handler(commands=['start'])
def stiker_Hi(message):
	sti = open('stickers/sticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Рэндоме')
	item2 = types.KeyboardButton('Наши проекты')
	item3 = types.KeyboardButton('Слитая инфаа!')

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, 'Добро пожаловать, мистер {0.first_name} {0.last_name}!\nЯ - <b>{1.first_name}</b>, бот для теста и проверки фотографий.'.format(message.from_user, bot.get_me()),
		parse_mode = 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def pressMarkup(message):
	if message.chat.type == 'private':
		if message.text == 'Рэндоме':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == 'Наши проекты':

			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton(project[0], callback_data=project[0])
			item2 = types.InlineKeyboardButton(project[1], callback_data=project[1])
			item3 = types.InlineKeyboardButton("Уйди", callback_data="close")

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Выбери один из них!', reply_markup=markup)
		elif message.text == 'Слитая инфаа!':
			for i in range(8):
				bot.send_message(message.chat.id, '<a href = "https://www.youtube.com'+ parser.href[i] + '">' + parser.title[i] + '</a>',
					parse_mode = 'html', reply_markup=None)
		else:
			bot.send_message(message.chat.id, 'Я ничего не понял(')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == project[0]:
				bot.send_message(chat_id=call.message.chat.id, text='Вот он:\n<a href="https://github.com/Goodenl/'+ project[0] +'.git">'+ project[0] +'</a>', parse_mode="html")

			elif call.data == project[1]:
				bot.send_message(chat_id=call.message.chat.id, text='Вот он:\n<a href="https://github.com/Goodenl/'+ project[1] +'.git">'+ project[1] +'</a>', parse_mode="html")

			#remove inline keyboard and text
			elif call.data == "close":
				bot.delete_message( call.message.chat.id, call.message.message_id )

			#show alert
				bot.answer_callback_query( callback_query_id=call.id, show_alert=False,
					text="Push Alert!!!" )

	except Exception as e:
		print(repr(e))

# run 
bot.polling(none_stop=True)