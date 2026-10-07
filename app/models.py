from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))

    animais = relationship("Animal", back_populates="tutor")


class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    raca = Column(String(50))
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=False)

    tutor = relationship("Tutor", back_populates="animais")
    atendimentos = relationship("Atendimento", back_populates="animal")


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    data = Column(Date, nullable=False)
    descricao = Column(String(200), nullable=False)

    animal = relationship("Animal", back_populates="atendimentos")