from datetime import date
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.models import Tutor, Animal, Atendimento


def criar_tutor(session: Session, nome: str, telefone: str, email: str | None = None) -> Tutor:
    tutor = Tutor(nome=nome, telefone=telefone, email=email)
    session.add(tutor)
    session.commit()
    return tutor


def criar_animal(session: Session, nome: str, especie: str, tutor_id: int,
                 raca: str | None = None, data_nascimento: date | None = None) -> Animal:
    animal = Animal(nome=nome, especie=especie, raca=raca,
                    data_nascimento=data_nascimento, tutor_id=tutor_id)
    session.add(animal)
    session.commit()
    return animal


def criar_atendimento(session: Session, animal_id: int, data: date,
                      descricao: str, valor: float) -> Atendimento:
    atendimento = Atendimento(animal_id=animal_id, data=data,
                              descricao=descricao, valor=valor)
    session.add(atendimento)
    session.commit()
    return atendimento


def listar_tutores(session: Session) -> list[Tutor]:
    return list(session.scalars(select(Tutor)))


def listar_atendimentos(session: Session) -> list[Atendimento]:
    return list(session.scalars(select(Atendimento).order_by(Atendimento.data)))


def total_por_tutor(session: Session):
    consulta = (
        select(Tutor.nome, func.sum(Atendimento.valor))
        .join(Animal, Animal.tutor_id == Tutor.id)
        .join(Atendimento, Atendimento.animal_id == Animal.id)
        .group_by(Tutor.nome)
    )
    return session.execute(consulta).all()