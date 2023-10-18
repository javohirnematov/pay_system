from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Ссылка на базу данных
# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'                                          # Это база на SQLite следующее на POSTGRES
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database/postgres'             # database название берем из docker-compose 5 строчка


# Подключение к базе данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Генерация сессий
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей(models.py)
Base = declarative_base()

# Импорт моделей
from database import models


# функция для генерации связей к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()