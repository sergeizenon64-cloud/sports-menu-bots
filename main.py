from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ТВОЙ_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("⚽ Футбол", callback_data="football")],
        [InlineKeyboardButton("🏒 Хоккей", callback_data="hockey")],
        [InlineKeyboardButton("🏀 Баскетбол", callback_data="basketball")],
        [InlineKeyboardButton("📅 Матчи сегодня", callback_data="today")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🏆 Спортивное меню",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "football":
        text = "⚽ Последние футбольные результаты"

    elif query.data == "hockey":
        text = "🏒 Последние хоккейные результаты"

    elif query.data == "basketball":
        text = "🏀 Последние результаты баскетбола"

    elif query.data == "today":
        text = "📅 Матчи сегодня"

    await query.edit_message_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("MENU BOT ЗАПУЩЕН")

app.run_polling()
