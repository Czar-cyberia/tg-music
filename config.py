from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "19341937"))
API_HASH = getenv("API_HASH", "63b7a382ae4056361d568322d4a46f89")
BOT_TOKEN = getenv("BOT_TOKEN","5124772364:AAGJ3VOHc-l9Ne-TDyBu4HgaZZSBzroI9ds")
BOT_NAME = getenv("BOT_NAME","Group Song Bot")
BOT_USERNAME = getenv("BOT_USERNAME", "Group_Vc_Song_Robot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dark_evil001")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Group_Vc_Song")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "AQBs-GGkD-juiWuR-au3ijh2Qys-K43_497jv1e2DbJPnEjJC04S6HzBS2aC8W6Vt5sAHopcs1YtRPmluOaq4x7EnY6y5r9FZHfO7u1tTvBvLX0nS0U8P9N7fYKPJrCI5THLLCCXX4Cyq8oh3RbCl4UbeOcQcZyhdtpzeHHyYSGuhd7xwAP48sbwxBu6xnlTjWbpi4SKrKEFphyPSlZe2Diyepyp_8Ya9nartkPFWlhMckMG8ixh4CocXp6z78071-SnrUzDVCp2Ic2B82n8sDnLJxY_pei2jVI1Y5DKArtXwC6ZHJ0w6ru5CM2qUQQYb-gnQtkoOk5UM4XAxUDwOayPAAAAATa99kAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "• / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5193860202").split()))
