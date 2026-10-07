from datetime import date

from app.database import SessionLocal, resetar_banco
from app import crud


def main():
    resetar_banco()

    with SessionLocal() as session:
        t1 = crud.criar_tutor(session, "Mariana Souza", "(61) 99999-1111", "mariana@email.com")
        t2 = crud.criar_tutor(session, "Carlos Lima", "(61) 98888-2222", "carlos@email.com")

        a1 = crud.criar_animal(session, "Thor", "Cachorro", t1.id, "Labrador", date(2020, 3, 10))
        a2 = crud.criar_animal(session, "Mel", "Gato", t1.id, "Siamês", date(2021, 7, 25))
        a3 = crud.criar_animal(session, "Bidu", "Cachorro", t2.id, "Poodle", date(2019, 1, 5))

        crud.criar_atendimento(session, a1.id, date(2026, 9, 1), "Vacina antirrábica", 80.0)
        crud.criar_atendimento(session, a1.id, date(2026, 9, 15), "Consulta de rotina", 120.0)
        crud.criar_atendimento(session, a2.id, date(2026, 9, 20), "Castração", 450.0)
        crud.criar_atendimento(session, a3.id, date(2026, 10, 2), "Limpeza dentária", 200.0)

        print("=== Tutores e seus animais ===")
        for tutor in crud.listar_tutores(session):
            print(f"{tutor.nome} -> {', '.join(a.nome for a in tutor.animais)}")

        print("\n=== Atendimentos ===")
        for at in crud.listar_atendimentos(session):
            print(f"{at.data} | {at.animal.nome} (tutor: {at.animal.tutor.nome}) "
                  f"| {at.descricao} | R$ {at.valor:.2f}")

        print("\n=== Total gasto por tutor ===")
        for nome, total in crud.total_por_tutor(session):
            print(f"{nome}: R$ {total:.2f}")


if __name__ == "__main__":
    main()