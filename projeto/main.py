from fastapi import FastAPI,  HTTPException, Path,Body,Depends
from sqlalchemy.orm import Session
from typing import Annotated
from database import SessionLocal, engine
import crud, models, schemas
from schemas import *
models.Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import Session
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

### GETS MEMBROS: 


@app.get("/membro/nome/{nome}", response_model=list[schemas.MembroCreate])
def listar_membros_por_nome(nome: Annotated[str, Path(title="Nome de um membro da academia",description="Escreva o nome do membro e receba uma lista com todos os membros que tem o nome escolhido", example="Fulano")], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_nome(db, nome)
    if membros_lista is None:
        detalhe = "Não tem nenhum membro com esse nome"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista


@app.get("/membro/ativo/{ativo}", response_model=list[schemas.MembroCreate])
def listar_membros_por_estado(ativo: Annotated[int, Path(title="Estado ativo ou inativo do membro",description="0 para membros inativos e 1 para membros ativos", example=1)], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_ativo(db, ativo)
    if membros_lista is None:
        detalhe = "Não tem nenhum membro com esse estado"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista


@app.get("/membro/plano/{plano_id}", response_model=list[schemas.MembroCreate])
def listar_membros_por_planoID(plano_id: Annotated[int, Path(title="Identificador do plano",description="Coloque o identificador que representa o id do plano que o membro faz parte", example="3")], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_plano_id(db, plano_id)
    if membros_lista is None:
        detalhe = "Não tem nenhum membro com esse plano"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista

@app.get("/membro/id/{membro_id}", response_model=schemas.MembroCreate)
def devolve_informacoes_do_membro(membro_id: Annotated[int, Path(title="Identificador do membro",description="Coloque o identificador que representa o id do membro", example=1)], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_id(db, membro_id)
    if membros_lista is None:
        detalhe = "Não tem nenhum membro com esse id"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista

@app.get("/membro/genero/{genero}", response_model=list[schemas.MembroCreate])
def devolve_informacoes_do_membro(genero: Annotated[str, Path(title="Gênero do membro",description="Digite o genero com o qual o membro se identifica", example="Feminino")], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_id(db, genero)
    if membros_lista is None:
        detalhe = "Não tem nenhum membro com esse genero"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista

@app.get("/membro/restricao_medica", response_model=list[schemas.MembroCreate])
def listar_membros_com_restricao(db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_restricao_medica(db)
    if membros_lista is None:
        detalhe = "Não existe ninguém com restrição médica"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista

@app.get("/membro/plano/nome/{nome}", response_model=list[schemas.MembroBase])
def listar_membros_do_plano_nome(nome: Annotated[str, Path(title="Nome do plano",description="Coloque o nome do plano para listar os membros que fazem parte do plano escolhido", example="Intensivo")], db: Session = Depends(get_db)):
    membros_lista = crud.get_membro_plano_nome(db, plano_nome=nome)
    if membros_lista is None:
        detalhe = "Não existe nenhum plano com esse nome ou Não existe ninguém cadastrado nesse plano"
        raise HTTPException(status_code=400, detail=detalhe,)
    return membros_lista

# ### GETS PERSONAIS
    
@app.get("/personal/personal_id/{personal_id}", response_model=schemas.PersonalBase)
def devolve_informacoes_do_personal(personal_id: Annotated[int, Path(title="Identificador do personal",description="Coloque o identificador que representa o id do personal", example=1)], db: Session = Depends(get_db)):
    personal_lista = crud.get_personal_id(db, personal_id)
    if personal_lista is None:
        detalhe = "Não tem nenhum personal com esse id"
        raise HTTPException(status_code=400, detail=detalhe,)
    return personal_lista

@app.get("/personal/genero/{genero}", response_model=list[schemas.PersonalBase])
def listar_personal_por_genero(genero: Annotated[str, Path(title="Gênero do personal",description="Digite o genero com o qual o personal se identifica", example="Masculino")], db: Session = Depends(get_db)):
    personal_lista = crud.get_personal_genero(db, genero)
    if personal_lista is None:
        detalhe = "Não tem nenhum personal com esse gênero"
        raise HTTPException(status_code=400, detail=detalhe,)
    return personal_lista

@app.get("/personal/personal_id/{personal_id}/membros", response_model=list[schemas.MembroBase])
def listar_membros_com_personal_id(personal_id: Annotated[int, Path(title="Identificador do personal",description="Coloque o identificador do personal para listar os membros que esse personal acompanha", example=1)], db: Session = Depends(get_db)):
    personal_lista = crud.get_personal_membros(db, personal_id)
    if personal_lista is None:
        detalhe = "Não existe um personal com esse id ou Nenhum membro tem esse personal"
        raise HTTPException(status_code=400, detail=detalhe,)
    return personal_lista
    
@app.get("/personal/nome/{nome}", response_model=list[schemas.PersonalBase])
def listar_personais_por_nome(nome: Annotated[str, Path(title="Nome de um personal da academia",description="Escreva o nome do personal e receba uma lista com todos os personais que tem o nome escolhido", example="Fulano")], db: Session = Depends(get_db)):
    personal_lista = crud.get_personal_nome(db, nome)
    if personal_lista is None:
        detalhe = "Não existe nenhum personal com esse nome"
        raise HTTPException(status_code=400, detail=detalhe,)
    return personal_lista
    
@app.get("/personal/membro/{membro_id}", response_model=list[schemas.PersonalBase])
def listar_personais_por_nome(membro_id: Annotated[int, Path(title="Identificador do membro",description="Coloque o identificador do membro para receber as informações do personal que acompanha o membro", example=1)], db: Session = Depends(get_db)):
    personal_lista = crud.get_personal_membro_id(db, membro_id)
    if personal_lista is None:
        detalhe = "Não existe um id para o personal ligado ao membro"
        raise HTTPException(status_code=400, detail=detalhe,)
    return personal_lista

# ### GET PLANOS
@app.get("/plano/plano_id/{plano_id}/membros", response_model=schemas.PlanoBase)
def listar_membro_do_plano_id(plano_id: Annotated[int, Path(title="Identificador do plano",description="Coloque o identificador do plano para receber a lista dos membros que estão nesse plano", example=1)], db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_id_membros(db, plano_id)
    if planos_lista is None:
        detalhe = "Não existe um plano com esse id ou Não existe um membro com esse plano"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

@app.get("/plano/nome/{nome}/membros", response_model=schemas.PlanoBase)
def listar_membro_do_plano_nome(nome: Annotated[str, Path(title="Nome do plano",description="Coloque o nome do plano para ver as informações do plano escolhido", example="basico")], db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_nome_membros(db, nome)
    if planos_lista is None:
        detalhe = "Não existe um plano com esse nome ou Não existe um membro com esse plano"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

@app.get("/plano/aulas_em_grupo", response_model=list[schemas.PlanoBase])
def listar_planos_com_aulas_em_grupo(db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_com_aulas_em_grupo(db)
    if planos_lista is None:
        detalhe = "Não há nenhuma aula em grupo"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

@app.get("/plano/id/{plano_id}", response_model=schemas.PlanoBase)
def informacoes_plano_id(plano_id: Annotated[int, Path(title="Identificador do plano",description="Coloque o identificador do plano para ver as informações do plano escolhido", example=1)], db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_id(db, plano_id)
    if planos_lista is None:
        detalhe = "Não existe um plano com o esse id"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

@app.get("/plano/nome/{nome}", response_model=list[schemas.PlanoBase])
def infomacoes_plano_nome(nome: Annotated[str, Path(title="Nome do plano",description="Coloque o nome do plano para ver as informações do plano escolhido", example="basico")], db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_nome(db, nome)
    if planos_lista is None:
        detalhe = "Não tem nenhum membro com esse nome"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

@app.get("/plano/promocao", response_model=list[schemas.PlanoBase])
def listar_planos_com_promocao(db: Session = Depends(get_db)):
    planos_lista = crud.get_plano_com_promocao(db)
    if planos_lista is None:
        detalhe = "Nao tem nenhum plano com promocao"
        raise HTTPException(status_code=400, detail=detalhe,)
    return planos_lista

# ### DELETES:
@app.delete("/membro/{membro_id}", response_model=list[MembroCreate])
def deletar_membro(membro_id: Annotated[int, Path(title="Identificador do membro",description="Coloque o identificador do membro para deletar o membro escolhido", example=1)], db: Session = Depends(get_db)):
    if crud.deletar_membro(db=db, membro_id=membro_id):
        return db.query(models.Membro).all()
    detalhe = "Não foi encontrado nenhum membro com esse id"
    raise HTTPException(status_code=400, detail=detalhe)

@app.delete("/personal/{personal_id}", response_model=list[PersonalCreate])
def deletar_personal(personal_id: Annotated[int, Path(title="Identificador do personal",description="Coloque o identificador do personal para deletar o personal escolhido", example=1)], db: Session = Depends(get_db)):
    if crud.deletar_personal(db=db, personal_id=personal_id):
        return db.query(models.Personal).all()
    detalhe = "Não foi encontrado nenhum personal com esse id"
    raise HTTPException(status_code=400, detail=detalhe)

@app.delete("/plano/{plano_id}", response_model=list[PlanoCreate])
def deletar_plano(plano_id: Annotated[int, Path(title="Identificador do plano",description="Coloque o identificador do plano para deletar o plano escolhido", example=1)], db: Session = Depends(get_db)):
    if crud.deletar_plano(db=db, plano_id=plano_id):
        return db.query(models.Plano).all()
    detalhe = "Não foi encontrado nenhum plano com esse id"
    raise HTTPException(status_code=400, detail=detalhe)

# # POSTS :

@app.post("/membro/", response_model=schemas.MembroBase)
def create_user(membro: Annotated[schemas.MembroBase,Body(description="Corpo para envio das informações para serem adicionadas")], db: Session = Depends(get_db)):
    return crud.create_membro(db=db, membro=membro)

@app.post("/plano/", response_model=schemas.PlanoCreate)
def create_plano(plano: Annotated[schemas.PlanoBase,Body(description="Corpo para envio das informações para serem adicionadas")], db: Session = Depends(get_db)):
    return crud.create_plano(db=db, plano=plano)

@app.post("/personal/", response_model=schemas.PersonalCreate)
def create_personal(personal: Annotated[schemas.PersonalBase,Body(description="Corpo para envio das informações para serem adicionadas")], db: Session = Depends(get_db)):
    return crud.create_personal(db=db, personal=personal)


# # PUTS :

@app.put("/membros/{membro_id}", response_model=schemas.MembroBase)
def update_membro(membro_id: int, membro_update: schemas.MembroUpdate, db: Session = Depends(get_db)):
    aux = crud.update_membro(membro_id=membro_id,db=db,membro_update=membro_update)
    if aux is None:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return crud.get_membro_id(db=db,membro_id=membro_id)

@app.put("/personal/{personal_id}", response_model=schemas.PersonalBase)
def update_personal(personal_id: int, personal_update: schemas.PersonalUpdate, db: Session = Depends(get_db)):
    aux = crud.update_personal(personal_id=personal_id,db=db,personal_update=personal_update)
    if aux is None:
        raise HTTPException(status_code=404, detail="Personal não encontrado")
    return crud.get_personal_id(db=db,personal_id=personal_id)

@app.put("/plano/{plano_id}", response_model=schemas.PlanoBase)
def update_plano(plano_id: int, plano_update: schemas.PlanoUpdate, db: Session = Depends(get_db)):
    aux = crud.update_plano(plano_id=plano_id,db=db,plano_update=plano_update)
    if aux is None:
        raise HTTPException(status_code=404, detail="plano não encontrado")
    return crud.get_plano_id(db=db,plano_id=plano_id)