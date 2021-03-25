import telegram
import logging
import downloadAnimes
import os

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

chat_id = 0
def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help(update, context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id, text=f"Last chat id:{chat_id}")

def downloadAll(update, context):
    chat_id=update.effective_chat.id
    url = context.args[0]
    # print(url)
    episode_list = downloadAnimes.getEpisodeList(url)
    # print(episode_list)
    for episode in episode_list:
        episode_link = downloadAnimes.getEpisodeLink(episode)
        # print(episode_link)

        file_name = url.split('/')[-1] + '_' + episode_link.split('/')[-1].split('-')[-1]

        episode_name = downloadAnimes.download(episode_link, file_name)

        file_path = os.getcwd() + '\\' + episode_name

        context.bot.send_document(chat_id, document=file_path, timeout=200)

def downloadTest(update, context):
    chat_id=update.effective_chat.id
    url = os.getcwd() + '\\log-horizon-entaku-houkai_AnV-01.mp4'
    #print(url)
    file = open(url, 'rb')
    #print(file)
    context.bot.send_document(chat_id, document=file, timeout=200)              


TOKEN = os.environ.get('TOKEN')
APPNAME = os.environ.get('APPNAME')
PORT = int(os.environ.get('PORT', '5000'))

updater = Updater(TOKEN, request_kwargs={'read_timeout': 600, 'connect_timeout': 600})
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.setWebhook("https://" + APPNAME + ".herokuapp.com/" + TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('downloadAll', downloadAll))
updater.dispatcher.add_handler(CommandHandler('downloadTest', downloadTest))

updater.start_polling(timeout=600, bootstrap_retries=3)
updater.idle()

    
    

   


   