import message_process as mp
import filters

from telegram.ext import *


# reading bot's token
TOKEN = None
with open('token', 'r') as f:
    TOKEN = f.read().strip()

# initialize updater
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# describing commands
handlers = (
    CommandHandler(
        'start',
        mp.start
    ),
    CommandHandler(
        'new',
        mp.new,
        filters=(filters.IsAdmin() & ~filters.IsFilling())
    ),
    CommandHandler(
        'pass',
        mp.miss,
        filters=(filters.IsAdmin() & filters.IsFilling() & filters.CanBeMissed())
    ),
    MessageHandler(
        (filters.IsAdmin() & filters.IsFilling()),
        mp.fill
    )
)

for h in handlers:
    dispatcher.add_handler(h)

# yeah, launching
updater.start_polling()

