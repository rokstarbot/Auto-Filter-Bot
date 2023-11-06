
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6897415564:AAGVZrqs-noK5VPdL1wLBZFygRtcgy7JGpA")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "23623198"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "2f71d58158f33d9560825858ab93434b")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQArPL3lZgoA0tfNaVGPn6m-G8xnMx-m9DJseOo4cYHKP7ro0DCiSG5SED1RTWIWY_cHJmY7WeT0ZRRRxz5EMPtyM4xvklqXNRirHORbr_A-f4--jNGxhJIiREGlKQulnIGeCdmwiEGz8zhRHUOIp3lQ0odkrQVle9gGmYVUYZpZDtQrzKa-P5P1VVliF0Th2oWGKO7cUFrK2QCts_Z1DeFAQJod4edz_ngII8WTAI6BzI-xwJkAsBDN4sRfD87dGj4kNtHceXT2bAE4r7kSDG0sYwltmKCoHY8HNUkHc3Won_mnkgICx4bT9I7MgcwTS2oQgv6ZsrhbZV-o_hGk1BAfAAAAAS99tzsA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001896066430")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
