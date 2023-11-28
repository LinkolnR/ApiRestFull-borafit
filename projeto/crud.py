from sqlalchemy.orm import Session

import models, schemas
### Função auxiliares com conexão com o banco de dados

# Membro
def get_membro_id(db: Session, membro_id: int):
    return db.query(models.Membro).filter(models.Membro.membro_id == membro_id).first()

def get_membro_nome(db: Session, nome: str):
    return db.query(models.Membro).filter(models.Membro.nome == nome).all()

def get_membro_ativo(db: Session, ativo: int):
    return db.query(models.Membro).filter(models.Membro.ativo == ativo).all()

def get_membro_genero(db: Session, genero: str):
    return db.query(models.Membro).filter(models.Membro.genero == genero).all()

def get_membro_plano_id(db: Session, plano_id: int):
    return db.query(models.Membro).filter(models.Membro.plano_id == plano_id).all()

def get_membro_restricao_medica(db: Session):
    return db.query(models.Membro).filter(models.Membro.restricao_medica != "nenhuma").all()


def get_membro_plano_nome(db: Session, plano_nome: str):
    aux = db.query(models.Plano).filter(models.Plano.nome == plano_nome).first()
    if aux is None:
        return None
    return db.query(models.Membro).filter(models.Membro.plano_id == aux.plano_id).all()


# Personal
def get_personal_id(db: Session, personal_id: int):
    return db.query(models.Personal).filter(models.Personal.personal_id == personal_id).first()

def get_personal_nome(db: Session, nome: int):
    return db.query(models.Personal).filter(models.Personal.nome == nome).all()

def get_personal_genero(db: Session, genero: int):
    return db.query(models.Personal).filter(models.Personal.genero == genero).all()

def get_personal_membros(db: Session, personal_id: int):
    aux = db.query(models.Personal).filter(models.Personal.personal_id == personal_id).first()
    if aux is None:
        return None
    return db.query(models.Membro).filter(models.Membro.personal_id == aux.personal_id).all()

def get_personal_membro_id(db: Session, membro_id: int):
    aux = db.query(models.Membro).filter(models.Membro.membro_id == membro_id).first()
    if aux is None:
        return None
    return db.query(models.Personal).filter(models.Personal.personal_id == aux.personal_id).all()


# Plano
def get_plano_id(db: Session, plano_id: int):
    return db.query(models.Plano).filter(models.Plano.plano_id == plano_id).first()

def get_plano_nome(db: Session, nome: str):
    return db.query(models.Plano).filter(models.Plano.nome == nome).all()

def get_plano_com_aulas_em_grupo(db: Session):
    return db.query(models.Plano).filter(models.Plano.aulas_em_grupo == 1).all()

def get_plano_com_promocao(db: Session):
    return db.query(models.Plano).filter(models.Plano.promocao == 1).all()

def get_plano_id_membros(db: Session, plano_id: int):
    aux = db.query(models.Plano).filter(models.Plano.plano_id == plano_id).first()
    if aux is None:
        return None
    return db.query(models.Membro).filter(models.Membro.plano_id == plano_id).all()

def get_plano_nome_membros(db: Session, nome: str):
    aux = db.query(models.Plano).filter(models.Plano.nome == nome).first()
    if aux is None:
        return None
    return db.query(models.Membro).filter(models.Membro.plano_id == aux.plano_id).all()

# Creates - POSTS
def create_membro(db: Session, membro: schemas.MembroCreate):
    db_membro = models.Membro(**membro.dict())
    db.add(db_membro)
    db.commit()
    db.refresh(db_membro)
    return db_membro


def create_personal(db: Session, personal: schemas.PersonalCreate):
    db_personal = models.Personal(**personal.dict())
    db.add(db_personal)
    db.commit()
    db.refresh(db_personal)
    return db_personal


def create_plano(db: Session, plano: schemas.PlanoCreate):
    db_plano = models.Plano(**plano.dict())
    db.add(db_plano)
    db.commit()
    db.refresh(db_plano)
    return db_plano


# Deletes

def deletar_membro(db: Session, membro_id: int):
    user_to_delete = db.query(models.Membro).filter(models.Membro.membro_id == membro_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return True
    return False

def deletar_personal(db: Session, personal_id: int):
    user_to_delete = db.query(models.Personal).filter(models.Personal.personal_id == personal_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return True
    return False

def deletar_plano(db: Session, plano_id: int):
    user_to_delete = db.query(models.Plano).filter(models.Plano.plano_id == plano_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return True
    return False

# Updates

def update_membro(db: Session, membro_id: int,membro_update: schemas.MembroUpdate):
    db_membro = db.query(models.Membro).filter(models.Membro.membro_id == membro_id).first()
    if db_membro is None:
        return None
    for key, value in membro_update.dict().items():
        setattr(db_membro, key, value)
    db.commit()
    db.refresh(db_membro)
    return True

def update_personal(db: Session, personal_id: int,personal_update: schemas.PersonalUpdate):
    db_personal = db.query(models.Personal).filter(models.Personal.personal_id == personal_id).first()
    print(db_personal)
    if db_personal is None:
        return None
    for key, value in personal_update.dict().items():
        setattr(db_personal, key, value)
    db.commit()
    db.refresh(db_personal)
    return True

def update_plano(db: Session, plano_id: int,plano_update: schemas.PlanoUpdate):
    db_plano = db.query(models.Plano).filter(models.Plano.plano_id == plano_id).first()
    print(db_plano)
    if db_plano is None:
        return None
    for key, value in plano_update.dict().items():
        setattr(db_plano, key, value)
    db.commit()
    db.refresh(db_plano)
    return True
