from datetime import date

from app import crud, models  # noqa: F401  (models precisa ser importado para criar as tabelas)
from app.database import Base, SessionLocal, engine


def main():
    # Recria as tabelas do zero (evita erro de coluna antiga no SQLite)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = SessionLocal()
    try:
        # Tutores
        t1 = crud.criar_tutor(session, "Igor Gabriel", "(61) 99999-1111", "igor.alves@email.com")
        t2 = crud.criar_tutor(session, "Sarah Isabela", "(61) 98888-2222", "sarah.isa@email.com")

        # Animais
        a1 = crud.criar_animal(session, "Thor", "Cachorro", "Labrador", t1.id)
        a2 = crud.criar_animal(session, "Mimi", "Gato", "Siamês", t1.id)
        a3 = crud.criar_animal(session, "Rex", "Cachorro", "Pastor Alemão", t2.id)

        # Atendimentos
        crud.criar_atendimento(session, a1.id, date(2026, 9, 1), "Vacina antirrábica")
        crud.criar_atendimento(session, a2.id, date(2026, 9, 3), "Consulta de rotina")
        crud.criar_atendimento(session, a3.id, date(2026, 9, 5), "Vermifugação")

        # Demonstração
        print("=== TUTORES ===")
        for t in crud.listar_tutores(session):
            print(f"{t.id} - {t.nome} | {t.telefone} | {t.email}")

        print("\n=== ANIMAIS ===")
        for a in crud.listar_animais(session):
            print(f"{a.id} - {a.nome} ({a.especie}, {a.raca}) | Tutor: {a.tutor.nome}")

        print("\n=== ATENDIMENTOS ===")
        for at in crud.listar_atendimentos(session):
            print(f"{at.id} - {at.data} | {at.animal.nome} | {at.descricao}")
    finally:
        session.close()


if __name__ == "__main__":
    main()