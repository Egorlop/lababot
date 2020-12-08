import telebot
import COVID19Py
from bs4 import BeautifulSoup
import requests
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1428515220:AAFQIAYTjATEnU_BIN95mVfwP9Nu4aQYsZs')
# def parse():
# 	URL = 'https://coronavirus-control.ru/coronavirus-russia/'
# 	HEADERS = {
# 		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 YaBrowser/20.11.2.78 Yowser/2.5 Safari/537.36'
# 	}
# 	response = requests.get(URL, headers=HEADERS)
# 	soup = BeautifulSoup(response.content, 'html.parser')
# 	convert = soup.findAll('span', {'class': 'plus'})
# 	stats = {
# 		'infectedday': convert[0].text,
# 		'letalday': convert[2].text,
# 		'recoveredday': convert[3].text
# 	}
# 	return stats
# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием



@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('В мире')
	btn2 = types.KeyboardButton('Россия')
	btn3 = types.KeyboardButton('Другая страна')
	btn4 = types.KeyboardButton('Памятка профилактики коронавируса')
	markup.add(btn1, btn2, btn3, btn4)

	send_message = f"<b>Привет, {message.from_user.first_name}!</b>\nЧтобы узнать данные по коронавирусу напишите " \
		f"название страны, например: США, Украина, Россия и так далее\n\n"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
	flag=0
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
	elif get_message_bot == "казахстан":
		location = covid19.getLocationByCountryCode("KZ")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "япония":
		location = covid19.getLocationByCountryCode("JP")
	elif get_message_bot == "в мире":
		flag=1
	elif get_message_bot == "памятка профилактики коронавируса":
		flag =4
	else:
		flag=-1
		final_message = "Введите название страны, чтобы получить подробную информацию"

	# if flag==2:
	# 	date = location[0]['last_updated'].split("T")
	# 	time = date[1].split(".")
	# 	stats = parse()
	# 	final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
	# 			f"Последние данные:\n" \
	# 			f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
	# 			f"{location[0]['latest']['deaths']:,}"\
	# 			# f"<b>Заболевших за день: </b>{stats['infectedday']}\n<b>Выздоровевших за день:</b> {stats['recoveredday']}\n"\
	# 			# f"<b>Смертей за день:</b> {stats['letalday']}\n"
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
	if flag == 4:
		pam1 = "<b>Правило 1:</b>\nЧистите и дезинфицируйте поверхности, используя бытовые моющие средства. Гигиена рук - это важная мера профилактики распространения гриппа и коронавирусной инфекции.\n"
		pam2 = "<b>Правило 2:</b>\nИзбегайте трогать руками глаза, нос или рот. Коронавирус, как и другие респираторные заболевания, распространяется этими путями. Надевайте маску или используйте другие подручные средства защиты, чтобы уменьшить риск заболевания. При кашле, чихании следует прикрывать рот и нос одноразовыми салфетками, которые после использования нужно выбрасывать.\n"
		pam3 = "<b>Правило 3:</b>\nЗдоровый образ жизни повышает сопротивляемость организма к инфекции. Соблюдайте здоровый режим, включая полноценный сон, потребление пищевых продуктов богатых белками, витаминами и минеральными веществами, физическую активность.\n"
		pam4 = "<b>Правило 4:</b>\nСреди прочих средств профилактики особое место занимает ношение масок, благодаря которым ограничивается распространение вируса.  "
		final_message = pam1 + pam2 + pam3 + pam4
	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)

