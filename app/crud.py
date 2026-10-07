from app.models import Animal, Atendimento, Tutor


def criar_tutor(session, nome, telefone=None, email=None):
    tutor = Tutor(nome=nome, telefone=telefone, email=email)
    session.add(tutor)
    session.commit()
    return tutor


def criar_animal(session, nome, especie, raca, tutor_id):
    animal = Animal(nome=nome, especie=especie, raca=raca, tutor_id=tutor_id)
    session.add(animal)
    session.commit()
    return animal


def criar_atendimento(session, animal_id, data, descricao):
    atendimento = Atendimento(animal_id=animal_id, data=data, descricao=descricao)
    session.add(atendimento)
    session.commit()
    return atendimento


def listar_tutores(session):
    return session.query(Tutor).all()


def listar_animais(session):
    return session.query(Animal).all()


def listar_atendimentos(session):
    return session.query(Atendimento).order_by(Atendimento.data).all()