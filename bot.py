from telegram.ext import Application, CommandHandler
import logging
import os

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    """دستور /start"""
    await update.message.reply_text('👋 سلام! ربات شما فعال است')

def main():
    # دریافت توکن از متغیر محیطی (ایمن‌ترین روش)
    TOKEN = os.getenv('BOT_TOKEN')  # یا توکن را مستقیماً اینجا قرار دهید
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("✅ ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
