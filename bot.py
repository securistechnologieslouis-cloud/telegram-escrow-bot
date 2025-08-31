import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")  # Le TOKEN sera ajouté dans Render (variable d'environnement)

ESCROWS = ["@User1", "@User2"]

async def escrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "ESCROW : " + " et ".join(ESCROWS)
    await update.message.reply_text(message)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("escrow", escrow))
    print("Bot démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()
