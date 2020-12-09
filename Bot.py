#Подключение библиотек, используемых в проиграмме
import telebot
import COVID19Py
from telebot import types
covid19 = COVID19Py.COVID19()


#Иницилизируем имя бота и передаем персональный токен
bot = telebot.TeleBot('1428515220:AAFQIAYTjATEnU_BIN95mVfwP9Nu4aQYsZs')

#Функция для обработки первого запуска бота пользвателем
@bot.message_handler(commands=['start'])
def start(message):
	#Создаем 4 функциональные клавиши
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('В мире')
	btn2 = types.KeyboardButton('Россия')
	btn3 = types.KeyboardButton('Другая страна')
	btn4 = types.KeyboardButton('Памятка профилактики коронавируса')
	markup.add(btn1, btn2, btn3, btn4)
	#Приветствие пользователя
	send_message = f"<b>Привет, {message.from_user.first_name}!</b>\n\nХочешь быть в курсе статистики по коронавирусу?\n\n" \
		f"Мы собираем для тебя самые свежие данные по количеству заболевших и количеству смертей во всём мире каждый день!\n\n"\
		"Используй @LabaCoronaBot, чтобы узнать статистику по странам из списка топ-15 по заражения COVID-19.\n\n" \
		"1) США\n2) Индия\n3) Бразилия\n4) Россия\n5) Франция\n6) Италия\n" \
		"7) Великобритания\n8) Испания\n9) Аргентина\n10) Колумбия\n11) Германия\n" \
		"12) Мексика\n13) Польша\n14) Иран\n15) Перу\n\n"\
		"<b>Читай наши советы по профилактике и будьте здоровы!</b>"
	#Отправка сообщения в чат
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
	#bot.send_message(message.chat.id, send_countries, parse_mode='html', reply_markup=markup)

# Функция, которая сработает при отправке какого-либо собщения боту
@bot.message_handler(content_types=['text'])
def mess(message):
	flag=0
	#Проверяем, какую страну ввёл пользователь, после чего присваиваем переменной location соответствующий тег
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "индия":
		location = covid19.getLocationByCountryCode("IN")
	elif get_message_bot == "бразилия":
		location = covid19.getLocationByCountryCode("BR")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "великобритания":
		location = covid19.getLocationByCountryCode("UK")
	elif get_message_bot == "испания":
		location = covid19.getLocationByCountryCode("ES")
	elif get_message_bot == "аргентина":
		location = covid19.getLocationByCountryCode("AR")
	elif get_message_bot == "колумбия":
		location = covid19.getLocationByCountryCode("CO")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "мексика":
		location = covid19.getLocationByCountryCode("MX")
	elif get_message_bot == "польша":
		location = covid19.getLocationByCountryCode("PL")
	elif get_message_bot == "иран":
		location = covid19.getLocationByCountryCode("IR")
	elif get_message_bot == "перу":
		location = covid19.getLocationByCountryCode("PE")
	elif get_message_bot == "в мире":
		flag=1
	elif get_message_bot == "памятка профилактики коронавируса":
		flag =2
	else:
		flag=-1
		final_message = "Введите название страны, чтобы получить подробную информацию"
	#В зависимости от значения переменной flag, переменная final_message будет иметь различное содержимое
	if flag == 1:
		location = covid19.getLatest()
		final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}"
	if flag == 0:
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
						f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
						f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
						f"{location[0]['latest']['deaths']:,}"
	if flag == 2:
		pam1 = "<b>Правило 1:</b>\nЧистите и дезинфицируйте поверхности, используя бытовые моющие средства. Гигиена рук - это важная мера профилактики распространения гриппа и коронавирусной инфекции.\n\n"
		pam2 = "<b>Правило 2:</b>\nИзбегайте трогать руками глаза, нос или рот. Коронавирус, как и другие респираторные заболевания, распространяется этими путями. Надевайте маску или используйте другие подручные средства защиты, чтобы уменьшить риск заболевания. При кашле, чихании следует прикрывать рот и нос одноразовыми салфетками, которые после использования нужно выбрасывать.\n\n"
		pam3 = "<b>Правило 3:</b>\nЗдоровый образ жизни повышает сопротивляемость организма к инфекции. Соблюдайте здоровый режим, включая полноценный сон, потребление пищевых продуктов богатых белками, витаминами и минеральными веществами, физическую активность.\n\n"
		pam4 = "<b>Правило 4:</b>\nСреди прочих средств профилактики особое место занимает ношение масок, благодаря которым ограничивается распространение вируса.  "
		final_message = pam1 + pam2 + pam3 + pam4
	# Отправка сообщения в чат
	bot.send_message(message.chat.id, final_message, parse_mode='html')
#Необходимо, чтобы бот не прекрощал свою работу по завершении цикла
bot.polling(none_stop=True)
