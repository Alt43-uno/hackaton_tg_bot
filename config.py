from aiogram import Bot, Dispatcher
import os
from db.db import Userdb, BannedUserdb
from environs import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='HTML')
CHAT_ADMIN = int(os.getenv('CHAT_ADMIN'))
CHAT_SUPPORT = int(os.getenv('CHAT_SUPPORT'))
ADMINS = [int(x) for x in os.getenv('ADMINS').split(',')]
dp = Dispatcher()

BASE_DIR = os.path.dirname(__file__)
PATH_TO_DB = os.path.join(BASE_DIR, 'db.db')

# SETTINGS
MIN_WITHDRAW = int(os.getenv('MIN_WITHDRAW'))
REF_PAY_ONE = float(os.getenv('REF_PAY_ONE'))

# DB
Users = Userdb()
BannedUsers = BannedUserdb()



