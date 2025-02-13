import os
import dotenv
from sqlalchemy import create_engine, text

# Carregar variáveis do .env
dotenv.load_dotenv()
db_url = os.getenv("DB_URL")

if not db_url:
    raise ValueError("DB_URL não está definido no arquivo .env")

engine = create_engine(db_url)


sql = text("SELECT name , type FROM books")
with engine.connect() as connection:
    result = connection.execute(sql)
    with open('books.txt', 'w') as f:
        for row in result.mappings():
            # Acessando as colunas pelo nome e gravando no arquivo
            f.write(f"{row['name']} - {row['type']}\n")