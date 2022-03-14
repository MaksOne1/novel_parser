import cloudscraper
from bs4 import BeautifulSoup
import telebot
from deep_translator import GoogleTranslator
import time

counter = 0

URL = 'https://www.novelupdates.com/latest-series/'
TOKEN = '5131120484:AAHvfkyh_x0Su6ENX3ddGjWGlrCO7h15qgY'
CHAT_ID = "-1001653032459"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

scraper = cloudscraper.create_scraper()

def main():
	data = scraper.get(URL).text
	soup = BeautifulSoup(data, 'html.parser')
	elements = soup.find_all('div', class_='search_main_box_nu')
	for element in elements:
		id = element.find('div', class_="search_title").find('span', class_="rl_icons_en").get('id')
		with open('keys.txt', 'r+') as f:
			info = f.read()
			if id not in info:
				f.write(f'{id}\n')

				image = element.find('div', class_="search_img_nu").find('img').get('src')
				href = element.find('div', class_="search_title").find('a').get('href')
				title = element.find('div', class_="search_title").find('a').text
				lang = element.find('div', class_="search_img_nu").find('span').text
				if lang == 'JP':
					lang = 'ja'
				elif lang == 'CN':
					lang = 'zh-CN'
				elif lang == "KR":
					lang = 'ko'
				rus = GoogleTranslator(source='auto', target='ru').translate(title) 
				original = GoogleTranslator(source='auto', target=lang).translate(title) 

				bot.send_message(CHAT_ID, f'Link: {href} \n English name: {title} \n Russian: {rus} \n Original name: {original} \n Image: {image}')
				time.sleep(15)

while True:
	counter += 1
	main()
	print(counter)
	time.sleep(120)




