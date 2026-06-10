import os
from dotenv import load_dotenv

load_dotenv()

EQUITYMIND_CORE_URL = os.getenv("EQUITYMIND_CORE_URL", "wss://equitymind.up.railway.app/api/v1/query/stream")
EQUITYMIND_CORE_KEY = os.getenv("EQUITYMIND_CORE_KEY", "")
APP_NAME = "EquityMind Web Backend"
