import os
import telebot
bot = telebot.TeleBot("6809579944:AAG5EVHBCkiPCr1o_CTptqWCHDyPkOX157Y")
user_new_names = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"""<b>Welcome to the file renamer bot. Send me a file to rename it.\nMade By @SH0NU</b>""",parse_mode="HTML") 
@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_name = message.document.file_name
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id, f"""<b>Current file name:</b> <code>{file_name}</code>\n<b>What should be the new name?</b>""",parse_mode="HTML")
    user_chat_id = message.chat.id
    user_new_names[user_chat_id] = (file_name, downloaded_file)
@bot.message_handler(func=lambda message: message.chat.id in user_new_names and user_new_names[message.chat.id] is not None)
def handle_new_name(message):
    original_file_name, downloaded_file = user_new_names[message.chat.id]
    new_name = message.text.strip()
    renamed_file_name = "" + new_name
    with open(renamed_file_name, 'wb') as renamed_file:
        renamed_file.write(downloaded_file)
    with open(renamed_file_name, 'rb') as renamed_file:
        bot.send_document(message.chat.id, renamed_file)
    del user_new_names[message.chat.id]
    os.remove(renamed_file_name)
bot.polling()
