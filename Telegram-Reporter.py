from telebot import TeleBot
import logging
import json
import os
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError, UserNotParticipantError, FloodWaitError
from telethon import functions
from telethon.tl import types

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot with the provided token
TOKEN = '6590125561:AAHd36L0bQ2E2APSgvPSKcDNu4OVqstW690'
bot = TeleBot(TOKEN)

# Function to save account details
def save_account(phone, api_id, api_hash):
    accounts = {}
    if os.path.exists('accounts.json'):
        with open('accounts.json', 'r') as f:
            accounts = json.load(f)
    
    accounts[phone] = {'api_id': api_id, 'api_hash': api_hash}
    
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Telegram Reporter Bot! Use /report to start reporting.")

@bot.message_handler(commands=['report'])
def report(message):
    bot.reply_to(message, "Please enter your phone number:")
    bot.register_next_step_handler(message, handle_phone)

def handle_phone(message):
    phone = message.text
    bot.reply_to(message, "Please enter your API ID:")
    bot.register_next_step_handler(message, handle_api_id, phone)

def handle_api_id(message, phone):
    api_id = message.text
    bot.reply_to(message, "Please enter your API Hash:")
    bot.register_next_step_handler(message, handle_api_hash, phone, api_id)

def handle_api_hash(message, phone, api_id):
    api_hash = message.text
    save_account(phone, api_id, api_hash)
    bot.reply_to(message, f"Account details saved for {phone}. Now enter the target ID (without @):")
    bot.register_next_step_handler(message, handle_target_id)

def handle_target_id(message):
    target_id = message.text
    bot.reply_to(message, f"Target ID set to {target_id}. Now enter the number of reports:")
    bot.register_next_step_handler(message, handle_num_reports, target_id)

def handle_num_reports(message, target_id):
    num_reports = int(message.text)
    bot.reply_to(message, "Choose a reporting method:\n1. Report Spam\n2. Report Other\n3. Report Violence\n4. Report Pornography\n5. Report Copyright")
    bot.register_next_step_handler(message, handle_report_method, target_id, num_reports)

def handle_report_method(message, target_id, num_reports):
    method = message.text
    report_function(target_id, num_reports, method)
    bot.reply_to(message, f"Reporting {target_id} with method {method} for {num_reports} times.")

def report_function(target_id, num_reports, method):
    # Load account details
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)
    
    # Assuming the phone number is the key
    phone = list(accounts.keys())[0]
    api_id = accounts[phone]['api_id']
    api_hash = accounts[phone]['api_hash']

    with TelegramClient('sessions/' + phone, api_id, api_hash) as client:
        for _ in range(num_reports):
            try:
                client(functions.account.ReportPeerRequest(
                    peer=target_id,
                    reason=types.InputReportReasonSpam(),
                    message="Reporting for spam."
                ))
                bot.send_message(target_id, f"Reported {target_id} for method {method}.")
            except Exception as e:
                bot.send_message(target_id, f"Error reporting {target_id}: {e}")

# Start polling
bot.polling()
