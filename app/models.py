from datetime import date
from sqlalchemy import ForeignKey, String, Date, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Tutor(Base):
    __tablename__ = "tutores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    telefone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(100), unique=True)

    animais: Mapped[list["Animal"]] = relationship(back_populates="tutor")


class Animal(Base):
    __tablename__ = "animais"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    especie: Mapped[str] = mapped_column(String(50))
    raca: Mapped[str | None] = mapped_column(String(50))
    data_nascimento: Mapped[date | None] = mapped_column(Date)
    tutor_id: Mapped[int] = mapped_column(ForeignKey("tutores.id"))

    tutor: Mapped["Tutor"] = relationship(back_populates="animais")
    atendimentos: Mapped[list["Atendimento"]] = relationship(back_populates="animal")


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[date] = mapped_column(Date)
    descricao: Mapped[str] = mapped_column(String(255))
    valor: Mapped[float] = mapped_column(Float)
    animal_id: Mapped[int] = mapped_column(ForeignKey("animais.id"))

    animal: Mapped["Animal"] = relationship(back_populates="atendimentos")