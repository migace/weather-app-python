from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()

API_KEY: Final[str] = os.getenv('API_KEY')
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'
