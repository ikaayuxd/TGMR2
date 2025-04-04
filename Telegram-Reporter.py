from telebot import TeleBot
import logging
import json
import os
from telethon.sync import TelegramClient
from telethon.errors import PhoneNumberBannedError, UserNotParticipantError, FloodWaitError
from telethon import functions
from telethon.tl import types

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot with the provided token
TOKEN = '6590125561:AAFmvRcEsiIjq3S3vazT8gqVScoKgomunzQ'
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
    phone = message.text.strip()
    bot.reply_to(message, "Please enter your API ID:")
    bot.register_next_step_handler(message, handle_api_id, phone)

def handle_api_id(message, phone):
    api_id = message.text.strip()
    bot.reply_to(message, "Please enter your API Hash:")
    bot.register_next_step_handler(message, handle_api_hash, phone, api_id)

def handle_api_hash(message, phone, api_id):
    api_hash = message.text.strip()
    save_account(phone, api_id, api_hash)

    bot.reply_to(message, f"Account details saved for {phone}. Please wait while we authenticate.")
    authenticate_user(phone, api_id, api_hash)

def authenticate_user(phone, api_id, api_hash):
    with TelegramClient('sessions/' + phone, api_id, api_hash) as client:
        client.start(phone)  # This triggers the authentication process
        # At this point, it handles OTP and other login features automatically

    bot.reply_to(message, f"Successfully logged in for {phone}. Now enter the target ID (without @):")
    bot.register_next_step_handler(message, handle_target_id)

def handle_target_id(message):
    target_id = message.text.strip()
    bot.reply_to(message, f"Target ID set to {target_id}. Now enter the number of reports:")
    bot.register_next_step_handler(message, handle_num_reports, target_id)

def handle_num_reports(message, target_id):
    try:
        num_reports = int(message.text.strip())
        bot.reply_to(message, "Choose a reporting method:\n1. Report Spam\n2. Report Other\n3. Report Violence\n4. Report Pornography\n5. Report Copyright")
        bot.register_next_step_handler(message, handle_report_method, target_id, num_reports)
    except ValueError:
        bot.reply_to(message, "Please enter a valid number for reports.")
        bot.register_next_step_handler(message, handle_num_reports, target_id)

def handle_report_method(message, target_id, num_reports):
    method = message.text.strip()
    report_function(target_id, num_reports, method)
    bot.reply_to(message, f"Reporting {target_id} with method {method} for {num_reports} times.")

def report_function(target_id, num_reports, method):
    # Load account details
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)

    phone = list(accounts.keys())[0]
    api_id = accounts[phone]['api_id']
    api_hash = accounts[phone]['api_hash']

    # Choose the report reason based on the method
    reason_mapping = {
        '1': types.InputReportReasonSpam(),
        '2': types.InputReportReasonOther(),
        '3': types.InputReportReasonViolence(),
        '4': types.InputReportReasonPornography(),
        '5': types.InputReportReasonCopyright(),
    }

    reason = reason_mapping.get(method)

    if reason is None:
        bot.send_message(phone, "Invalid reporting method selected.")
        return

    with TelegramClient('sessions/' + phone, api_id, api_hash) as client:
        for _ in range(num_reports):
            try:
                client(functions.account.ReportPeerRequest(
                    peer=target_id,
                    reason=reason,
                    message="Reporting due to selected reason."
                ))
                bot.send_message(phone, f"Successfully reported {target_id} for method {method}.")
            except FloodWaitError as e:
                bot.send_message(phone, f"Flood wait error: {e}. Please wait before reporting again.")
                break
            except Exception as e:
                bot.send_message(phone, f"Error reporting {target_id}: {e}")
                break

# Start polling
bot.polling()
