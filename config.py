# Copyright (C) @Wolfy004
# Channel: https://t.me/Wolfy004

import os
from time import time
from dotenv import load_dotenv

load_dotenv("config.env")

class PyroConf:
    try:
        API_ID = int(os.getenv("API_ID", "0"))
    except ValueError:
        API_ID = 0

    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv("MONGODB_URI", "")

    try:
        OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    except ValueError:
        OWNER_ID = 0

    FORCE_SUBSCRIBE_CHANNEL = os.getenv("FORCE_SUBSCRIBE_CHANNEL", "")

    # Payment and Contact Configuration
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
    PAYPAL_URL = os.getenv("PAYPAL_URL", "")
    UPI_ID = os.getenv("UPI_ID", "")
    
    # Ad Monetization - Multiple Ad Types
    # Each AD_ID can contain multiple zone IDs (comma-separated) for random rotation
    AD_ID_1 = os.getenv("AD_ID_1", "")  # Type 1: Interstitial/Popup ads
    AD_ID_2 = os.getenv("AD_ID_2", "")  # Type 2: Banner ads
    AD_ID_3 = os.getenv("AD_ID_3", "")  # Type 3: Video/Native ads
    VERIFICATION_ID = os.getenv("VERIFICATION_ID", "")  # Human verification zone ID

    BOT_START_TIME = time()
