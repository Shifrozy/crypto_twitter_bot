from telegram.ext import Updater, CommandHandler
import yaml

config = yaml.safe_load(open("config.yaml"))

def start(update, context):
    update.message.reply_text("Hello boss! Ready to scan Twitter & transact 🚀")

def set_amount(update, context):
    chain = context.args[0]
    amount = float(context.args[1])
    config['default_amounts'][chain] = amount
    update.message.reply_text(f"Amount for {chain} set to {amount}")

def run_telegram():
    updater = Updater(token=config['telegram_token'], use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set_amount", set_amount))
    
    updater.start_polling()
    print("Telegram bot running...")
    updater.idle()