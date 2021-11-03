import os

from dotenv import load_dotenv

load_dotenv()

dsl = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT')
}


if __name__ == '__main__':
    print(dsl)