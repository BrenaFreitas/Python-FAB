import os
import dotenv
from main import DatabaseExtrator  

dotenv.load_dotenv()
db_url = os.getenv("DB_URL")

if not db_url:
    raise ValueError("DB_URL não está definido no arquivo .env")

generator = DatabaseExtrator(db_url)
response = generator.process_file()

print(response["message"]) 
