import os
import telebot
from telebot import types

BOT_API_TOKEN = "6809579944:AAEbyPSMRT1PnUmL3o4epNYWB7yNKLVU04w"
CHANNEL_USERNAME = "SH0NU_TOOLS"
CREATOR_USERNAME = "SH0NU"


bot = telebot.TeleBot(BOT_API_TOKEN)
user_new_names = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create an inline keyboard
    keyboard = types.InlineKeyboardMarkup()
    
    # Add buttons to the keyboard (each button in a new row)
    channel_button = types.InlineKeyboardButton("Join Channel❤️‍🩹", url=f"https://t.me/{CHANNEL_USERNAME}")
    creator_button = types.InlineKeyboardButton("Creator❤️‍🩹", url=f"https://t.me/{CREATOR_USERNAME}")
    share_bot_button = types.InlineKeyboardButton("Share Bot❤️‍🩹", switch_inline_query=f"Check out this file renamer bot: @{bot.get_me().username}")

    # Add buttons to the keyboard layout (each button in a new row)
keyboard.add(channel_button, creator_button)
    keyboard.add(share_bot_button)

    # Send the welcome message with the inline keyboard
    bot.reply_to(message, f"""<b>Welcome to the file renamer bot. Send me a file to rename it.Made By @SH0NU</b>""", parse_mode="HTML", reply_markup=keyboard)

@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_name = message.document.file_name
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id, f"""<b>Current file name:</b> <code>{file_name}</code>\n<b>What should be the new name?</b>""", parse_mode="HTML")
    user_chat_id = message.chat.id
    user_new_names[user_chat_id] = (file_name, downloaded_file)

@bot.message_handler(func=lambda message: message.chat.id in user_new_names and user_new_names[message.chat.id] is not None)
def handle_new_name(message):
    original_file_name, downloaded_file = user_new_names[message.chat.id]
    new_name = message.text.strip()
    renamed_file_name = "" + new_name
    with open(renamed_file_name, 'wb') as renamed_file:
        renamed_file.write(downloaded_file)

    # Send the renamed file with channel name, creator name, and user name
    with open(renamed_file_name, 'rb') as renamed_file:
        # Send the document with a "Share Bot" inline button
        share_bot_button = types.InlineKeyboardButton("Share Bot❤️‍🩹", switch_inline_query=f"Check out this file renamer bot: @{bot.get_me().username}")
        inline_keyboard = types.InlineKeyboardMarkup().add(share_bot_button)
        
        bot.send_document(
            message.chat.id,
            renamed_file,
            caption=f"File renamed by @{message.from_user.username}\nChannel: @{CHANNEL_USERNAME}\nCreator: @{CREATOR_USERNAME}",
            reply_markup=inline_keyboard
        )

    # Send the renamed file without additional caption
    with open(renamed_file_name, 'rb') as renamed_file:
        bot.send_document(message.chat.id, renamed_file)
        bot.reply_to(message, f"""<b>Uploaded Successfully, 
Thanks For Using Me! 💗\n\n@SH0NU</b>""", parse_mode="HTML")

    del user_new_names[message.chat.id]
    os.remove(renamed_file_name)

# Polling for updates
bot.polling()
