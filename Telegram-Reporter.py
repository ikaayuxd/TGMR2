from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError, UserNotParticipantError, FloodWaitError
from telethon import functions
from telethon.tl import types
from prettytable import PrettyTable
from colorama import init, Fore
import os
import sys
import asyncio
import json

init()

def clear():
    os.system("cls || clear")

colors = {
    "red": '\033[00;31m',
    "green": '\033[00;32m',
    "light_green": '\033[01;32m',
    "yellow": '\033[01;33m',
    "light_red": '\033[01;31m',
    "blue": '\033[94m',
    "purple": '\033[01;35m',
    "cyan": '\033[00;36m',
    "grey": '\033[90m',
    "reset": Fore.RESET,
    "light_green_ex": Fore.LIGHTGREEN_EX,
    "white": Fore.WHITE,
}

messages = {
    "info": f"{colors['red']}[{colors['light_green']}+{colors['red']}] {colors['light_green']}",
    "error": f"{colors['red']}[{colors['light_red']}-{colors['red']}] {colors['light_red']}",
    "success": f"{colors['green']}All messages sent successfully!{colors['reset']}",
}

clear()

_ = input(f"{colors['red']}[{colors['green']}1{colors['red']}] {colors['green']}Telegram Reporter Free\n\n{colors['red']}[{colors['green']}2{colors['red']}] {colors['green']}Telegram Reporter Vip\n\n\tSelect: {colors['cyan']}")

if _ == '2':
    print (f"""
{colors['green']}                
Telegram Reporter 💣

Features: 
{colors['cyan']}
Add unlimited accounts ✅

Manage accounts ✅

Send reports with one or more accounts ✅

Block with one or more accounts ✅

Send spam with one or more accounts ✅

Send reports to site support ✅

Send reports to support email ✅

Written in Python and open source with free updates ♻️

Payment method: Crypto (Usdt, btc, ltc, etc... and Git card)

{colors['yellow']} Buy: https://t.me/esfelorm
""")
    exit()
clear()
if not os.path.exists('sessions'):
    os.makedirs('sessions')

def save_account(phone, api_id, api_hash):
    accounts = {}
    if os.path.exists('accounts.json'):
        with open('accounts.json', 'r') as f:
            accounts = json.load(f)
    
    accounts[phone] = {'api_id': api_id, 'api_hash': api_hash}
    
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f)



async def authenticate_client(client, phone):
    if not await client.is_user_authorized():
        try:
            await client.send_code_request(phone)
            code = input(f"{messages['info']}Enter the login code for {colors['white']}{phone}{colors['red']}: ")
            await client.sign_in(phone, code)
        except PhoneNumberBannedError:
            print(f"{messages['error']}{phone} is banned!{colors['reset']}")
            sys.exit()

async def get_user_info(client, username, method, typereport):
    clear()
    print (f'''{colors["cyan"]}
                @@                                                               @@            
               @@@@                                                              @@@          
              @@@@@                                                             @@@@@         
               @@@@@                                                           @@@@@          
                @@@@@@                                                       @@@@@@           
                 @@@@@@                                                     @@@@@@            
                  @@@@@@                                                   @@@@@@             
                @@ @@@@                                                     @@@@ @@           
               @@@@@@@                                                       @@@@@@@          
             @@@@@@@@                                                         @@@@@@@@        
            @@@@@@@                                                             @@@@@@@       
           @@@@@@@@                       {colors["white"]}Telegram: @Mresfelurm{colors["cyan"]}                 @@@@@@@@      
          @@@@@@@@@@                                                           @@@@@@@@@@     
         @@@@@@@@@@@@ @                       @@@@@@@                       @ @@@@@@@@@@@     
         @@@@@@@@@@@ @@@@                 @@@@@@@@@@@@@@@                 @@@@ @@@@@@@@@@@    
         @@@@@@@@@@@@@@@  @@@@    @@@@@@@@@@@@@@@@@    @@@@@@@@@@    @@@@  @@@@@@@@@@@@@@@    
          @@@@@@@@@@@@@@ @@@@  @@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@  @@@@ @@@@@@@@@@@@@@     
           @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@  @@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@      @@@      @@@@@@ @@@@@@@@@@@@@         
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@           
                   @@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@              
                     @@@@@@@@@@@@@@@@@@@@                        @@@@@@@@@@@@@                
                        @@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@                   
                          @@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@                     
                          @@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@                     
                        @@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@                   
                          @@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@                     
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @                        
                             @ @@@    @@@@@@@@@@@@@@@@@@@@      @@@@                          
                               @@@         @@@@@@@@@@@          @@@@@                         
                          @   @@@@           @@@@@@@@           @@@@@@  @                     
                         @@@@@@@@@@@       @@@@@@@@@@@@@       @@@@@@@@@@@                    
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
                          @@@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@@@@@@@@@@@@@                     
                           @@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@                      
                           @@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@                      
                            @@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@                       
                               @@@@  @@@@@@@@@@@@@ @@@@@@@@@@@  @@@@                          
                                      @@@@@@@@@@@@@@@@@@@@@@@                                 
                                     @@@@@@@@@@@@@@@@@@@@@@@@@                                
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@                               
                                     @@@@@@@@@@@@@@@@@@@@@@@@@                                
                                      @@@@@ @@@@@ @@@@@ @@@@@                                 
                                       @@@@  @@@@ @@@@  @@@@                                  
                                       @@@@  @@@@ @@@   @@@                                   
                                        @@    @@@ @@     @                                    
                                         @     @@ @                                           
                                                @                                             
''')
    __import__("time").sleep(3)
    try:
        entity = await client.get_entity(username)
        response = ""

        if hasattr(entity, 'first_name'):
            response += f"{messages['info']}Account Name: {entity.first_name} {entity.last_name or ''}\n"
            response += f"{messages['info']}Numeric ID: {entity.id}\n"
            response += f"{messages['info']}ID: @{username}\n"
            response += f"{messages['info']}Phone: {entity.phone or 'N/A'}\n"
            response += f"{messages['info']}Bot: {'Yes' if entity.bot else 'No'}\n"
        elif hasattr(entity, 'title'):
            response += f"{messages['info']}Channel/Group Name: {entity.title}\n"
            response += f"{messages['info']}Numeric ID: {entity.id}\n"
            response += f"{messages['info']}ID: @{username}\n"
            res = await client(functions.channels.GetFullChannelRequest(entity))
            response += f"{messages['info']}Member Count: {res.full_chat.participants_count}\n"
        else:
            print(f"{messages['error']}This username does not correspond to a user or channel/group.")
            return

        response += f"{messages['info']}Report Method: {method}\n"
        response += f"{messages['info']}Number of Reports: {typereport}\n"

        print(f'{colors["yellow"]}{"+" * 50}\n{colors["green"]}INFO Target:\n{response}{colors["yellow"]}{"+" * 50}\n')
    except Exception as e:
        print(f"{messages['error']}Error retrieving user info: {e}")

async def report(client, recipient, num_messages, method, text=None):
    try:
        channel_entity = await client.get_entity(recipient)
        
        reasons = {
            "1": types.InputReportReasonSpam(),
            "2": types.InputReportReasonOther(),
            "3": types.InputReportReasonViolence(),
            "4": types.InputReportReasonPornography(),
            "5": types.InputReportReasonCopyright(),
            "6": types.InputReportReasonSpam(),
            "7": types.InputReportReasonGeoIrrelevant(),
            "8": types.InputReportReasonIllegalDrugs(),
            "9": types.InputReportReasonPersonalDetails(),
        }

        message_dict = {
            "1": "This channel contains spam content.",
            "2": input(f"{messages['info']}Enter your message: {colors['grey']}"),
            "3": "This channel contains violent content.",
            "4": "This channel has pornographic content.",
            "5": "Block this channel due to copyright.",
            "6": "Block this channel due to scam and impersonation.",
            "7": "Block this channel due to irrelevant geo.",
            "8": "Block this channel because of Illegal Drugs.",
            "9": "Block this channel because of Personal Details.",
        }

        for _ in range(num_messages):
            await client(functions.account.ReportPeerRequest(
                peer=channel_entity,
                reason=reasons[method],
                message=message_dict[method]
            ))
            print(f"{messages['info']}report has been sent for method {method}")
    except FloodWaitError as e:
        print(f"{messages['error']}Too many requests. Please wait {e.seconds} seconds.")
    except UserNotParticipantError:
        print(f"{messages['error']}You are not a member of this channel/group.")
    except Exception as e:
        print(f"{messages['error']}Error during reporting: {e}")

async def reporter_channel(accounts):
    phone = input(f"{messages['info']}Enter your phone number: {colors['cyan']}")
    accounts = {}
    
    if os.path.exists('accounts.json'):
        with open('accounts.json', 'r') as f:
            accounts = json.load(f)

    if phone in accounts:
        api_id = accounts[phone]['api_id']
        api_hash = accounts[phone]['api_hash']
    else:
        api_id = input(f"{messages['info']}Enter your API ID: {colors['cyan']}")
        api_hash = input(f"{messages['info']}Enter your API Hash: {colors['cyan']}")
        save_account(phone, api_id, api_hash)
    clear()
    recipient = input(f'''{colors["grey"]}                                                                                                                                                                                                  
                               @@@@@@@@@@@@@@@                                          
  @                         @@@@@@@@     @@@@@@@@                         @             
  @@@                     @@@@@@@@   @@@   @@@@@@@@                     @@@             
   @@@@@@              @@@@@@@@@@  @@   @@  @@@@@@@@@@              @@@@@@              
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@     @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
      @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@     @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                        @@@@@@@@@@  @@@@@  @@@@@@@@@@                                   
                         @@@@  @@@@@     @@@@@  @@@@                                    
                         @@@@    @@@@@@@@@@@    @@@@ {colors["green"]}Telegram Reporter{colors["grey"]}                                   
                        @@@@@      @@@@@@@      @@@@                                    
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                   
                          @@@@@@@@@@@@ @@@@@@@@@@@@    {colors["red"]}Version 1{colors["grey"]}                               
                           @@   @@@@  @  @@@@   @@                                      
                                @@@@@@@@@@@@@                                           
                                 @@@@@@@@@@@   {colors["yellow"]}Telegram: @MrEsfelurm{colors["grey"]}                                         
                                 @@ @@@@@ @@                                            
                                  @ @@ @@ @                                             
                                     @ @                                                
                                                                                                
{messages["info"]}Enter the target ID (without @): {colors["cyan"]}''')
    num_messages = int(input(f'{messages["info"]}Number of reports: {colors["red"]}'))

    methods_table = PrettyTable([f'{colors["cyan"]}Number{colors["red"]}', f'{colors["cyan"]}Method{colors["red"]}'])
    methods = {
        "1": "Report Spam",
        "2": "Report Other",
        "3": "Report Violence",
        "4": "Report Pornography",
        "5": "Report Copyright",
        "6": "Report Fake",
        "7": "Report Geo Irrelevant",
        "8": "Report Illegal Drugs",
        "9": "Report Personal Details"
    }

    for number, method in methods.items():
        methods_table.add_row([f'{colors["red"]}{number}{colors["red"]}', f'{colors["green"]}{method}{colors["red"]}'])

    print(methods_table)
    method = input(f"{messages['info']}Choose a method: {colors['cyan']}")


    async with TelegramClient(f'sessions/{phone}', api_id, api_hash) as client:
        await authenticate_client(client, phone)
        await get_user_info(client, recipient, method, num_messages)
        await report(client, recipient, num_messages, method)

asyncio.run(reporter_channel([]))
