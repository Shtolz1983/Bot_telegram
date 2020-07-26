import telebot
import datetime
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

date =str(datetime.datetime.today().date())
url = "https://api.nasa.gov/planetary/apod"

payload = {'date': date, 'hd': 'bool', 'api_key': 'ulpmHwaZnRbTY22axukFIXy4Uc2qKAPKUlnCkv7C'}
response = requests.request("GET", url, params=payload)

url_bot = response.json()['url']
text_bot =response.json()['explanation']
bot = telebot.TeleBot('1073569376:AAFXWbFgho9Q3r4zODyDqWvSvuLg2bIUPCI')
id = '-1001463284489'

@sched.scheduled_job('cron', day_of_week ='mon-sun' , hour=12)
def job():
    return bot.send_photo(id, url_bot), bot.send_message(id, text_bot)
sched.start()

