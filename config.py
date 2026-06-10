import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "EquityMind Web Backend"

# equitymind-core connection
EQUITYMIND_CORE_URL = os.getenv("EQUITYMIND_CORE_URL")
EQUITYMIND_CORE_KEY = os.getenv("EQUITYMIND_CORE_KEY")
