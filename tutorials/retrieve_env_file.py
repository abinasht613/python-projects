from dotenv import load_dotenv
import os

load_dotenv()
# load_dotenv(dotenv_path='/path/to/your/.env')

print(f"{os.getenv('API_KEY')}")