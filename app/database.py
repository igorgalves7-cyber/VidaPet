from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

engine = create_engine("sqlite:///vidapet.db")
SessionLocal = sessionmaker(bind=engine)


def criar_tabelas():
    Base.metadata.create_all(engine)


def resetar_banco():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)