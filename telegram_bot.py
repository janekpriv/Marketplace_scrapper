import asyncio  # Dodaj ten import na początku pliku
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import threading
import time
import os
import sys
from olx_search import olxSearcher
from facebook import FacebookSearcher
from evaluate_model import *
from sumarized import *

TELEGRAM_BOT_TOKEN = "7828773314:AAEkF_vIyhLdHLa8196QgnvVAUWhR6Bv5Dc"
CHAT_IDS_FILE = "chat_ids.txt"

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


# Funkcja do cyklicznego sprawdzania i wysyłania aktualizacji
async def check_and_send_updates(application):
    while True:
        print("Sprawdzanie nowych danych...")
        csv_files = os.listdir('phones_csv')
        if "iphone16_list_OLX.csv" in csv_files:
            file_path = os.path.join('phones_csv', "iphone16_list_OLX.csv")
            with open(file_path, 'rb') as file:
                if os.path.exists(CHAT_IDS_FILE):
                    with open(CHAT_IDS_FILE, "r") as chat_file:
                        chat_ids = [line.split(",")[0].strip() for line in chat_file.readlines()]
                    for chat_id in chat_ids:
                        try:
                            await application.bot.send_message(chat_id=int(chat_id), text="Znaleziono nowe dane dla iPhone 16!")
                            await application.bot.send_document(chat_id=int(chat_id), document=file)
                        except Exception as e:
                            print(f"Nie udało się wysłać wiadomości do chat_id {chat_id}: {e}")
        await asyncio.sleep(60)

# Funkcja startowa z przyciskami
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Tak", callback_data="subscribe_yes"),
         InlineKeyboardButton("Nie", callback_data="subscribe_no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Czy chcesz zapisać się na powiadomienia o nowych danych? 📩",
        reply_markup=reply_markup
    )

# Funkcja obsługująca przyciski
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id
    user_name = query.from_user.full_name

    if query.data == "subscribe_yes":
        if not os.path.exists(CHAT_IDS_FILE) or f"{chat_id}, {user_name}" not in open(CHAT_IDS_FILE).read():
            with open(CHAT_IDS_FILE, "a") as file:
                file.write(f"{chat_id}, {user_name}\n")
            await query.edit_message_text("Dziękujemy! Zostałeś zapisany na powiadomienia. ✅")
        else:
            await query.edit_message_text("Już jesteś zapisany na powiadomienia. ✅")
    elif query.data == "subscribe_no":
        await query.edit_message_text("Rozumiem, nie zostałeś zapisany na powiadomienia. ❌")

# Główna funkcja bota
async def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Uruchamianie funkcji cyklicznej w tle
    asyncio.create_task(check_and_send_updates(application))

    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Start bota
    await asyncio.Event().wait()


# if __name__ == "__main__":
#     try:
#         loop = asyncio.get_running_loop()
#         if loop.is_running():
#             print("Pętla asyncio już działa. Uruchamiam zadanie.")
#             loop.create_task(main())
#         else:
#             loop.run_until_complete(main())
#     except RuntimeError:
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#         loop.run_until_complete(main())

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot zatrzymany.")