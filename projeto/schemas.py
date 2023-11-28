from pydantic import BaseModel, Field  
from datetime import datetime ,date

model_config_Membro = {

        "json_schema_extra": {
            "examples": [
                {
                    "nome" : "Raul",
                    "sobrenome" : "Seixas",
                    "genero" : "Masculino",
                    "cpf" : "66569678302",
                    "plano_id" : 2,
                    "ativo": 1,
                    "telefone": "11940028922",
                    "email": "exemplo@exemplo.com",
                    "personal_id": 1,
                    "restrição_medica": "nenhuma"
                }
            ]
        }
    }

class MembroBase(BaseModel):
    nome: str = Field(min_length = 2, description="Nome precisa ter pelo menos duas letras",examples=["Fulano"])
    sobrenome: str | None = None
    genero: str = Field(min_length = 5, description="Genero precisa ter pelo menos cinco letras",examples=["Não definido"])
    cpf: str = Field(pattern=r'^\d*$', max_length=11, min_length=11,description="O cpf deve ter 11 dígitos, não inclua os pontos ( . ) e nem o traço ( - )", examples=["01234567891"]) # pattern só permite números
    plano_id: int = Field( description="Identificador do plano na qual a pessoa está matriculada", examples =[1])
    ativo: int = Field( description="0: se o membro não está ativo e 1: se o membro está ativo", examples =[0])
    telefone: str | None = Field(pattern=r'^\d*$', min_length=11, max_length=11,description="O telefone deve ter 11 dígitos (2)DDD+9+número(8) , sem espaços!",  examples=["98765432100"])
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',description="O email deve ser válido" ,examples=["exemplo@email.com"])
    personal_id: int | None = Field(gt=0, description="Colocando o id do personal", examples =[1], default=None)
    restricao_medica: str | None = Field(description="Informações sobre restrições médicas a serem seguidas por um membro", examples =["Problema no joelho"], default="nehuma")
    data_inscricao: date = Field(default = datetime.now().date(), description="Colocando a data atual, ou seja, a hora do cadastro")
    ultima_presenca: date | None = Field(default = None, description="Ultimo dia que o membro frequentou a academia")
    class Config:
        from_attributes = True
        json_schema = model_config_Membro["json_schema_extra"]
    
class MembroCreate(MembroBase):
    membro_id: int | None

model_config_plano = {
    "json_schema_extra": {
        "examples": [
            {
                "nome" : "Basic",
                "description": "Plano Basic",
                "preco": 100.0,
                "aulas_em_grupo": 0,
                "promocao": 1
            }
        ]
    }
}

class PlanoBase(BaseModel):
    nome: str 
    descricao: str | None = Field( description="Mais detalhes sobre o plano",examples=["Plano mais completo com acompanhamento"])
    preco: float = Field(gt=0, description="O preço precisa ser maior que zero!",examples=[100])
    aulas_em_grupo: int =Field(lt=2, description="0: se não oferece aulas em grupo e 1: se oferece aulas em grupo", examples = [0])
    promocao: int = Field( lt=2,description="0: se o plano não está em promoção e 1: se o plano está em promoção",  examples = [1])
    class Config:
        from_attributes = True
        json_schema = model_config_plano["json_schema_extra"]

class PlanoCreate(PlanoBase):
    plano_id: int | None

model_config_personal = {
    "json_schema_extra": {
        "examples": [
            {
                "nome" : "Amethysta",
                "sobrenome": "Perola",
                "membro_id": 2,
                "cpf": "11223344556",
                "genero": "Feminino",
                "telefone": "23919283746",
                "email": "amethypearl@borafit.com",
                "salario": 3000.0
            }
        ]
    }
}

class PersonalBase(BaseModel):
    nome : str = Field(min_length = 2, description="Nome precisa ter pelo menos duas letras", default=None, examples=["Roberta"])
    sobrenome: str 
    membro_id : int | None = Field(description= "Uma lista com os identificadores dos membros da academia que o personal acompanha",examples=[2])
    cpf: str = Field(pattern=r'^\d*$', max_length=11, min_length=11,description="O cpf deve ter 11 dígitos, não inclua os pontos ( . ) e nem o traço ( - )",examples=["01234567891"]) # pattern só permite números
    genero: str 
    telefone: str = Field(pattern=r'^\d*$', max_length=11,description="O telefone deve ter 11 dígitos DDD+9+número , sem espaços!",examples=["11999523499"])
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',description="O email deve ser válido", examples=["exemplo@dominio.com"])
    salario: float = Field(gt=0, description="O salário precisa ser maior que zero!", examples=[2000.0])
    class Config:
        from_attributes = True
        json_schema = model_config_plano["json_schema_extra"]

class PersonalCreate(PersonalBase):
    personal_id: int | None

model_config_membro_update = {
    "json_schema_extra": {
        "examples": [
            {
                "plano_id" : 1,
                "personal_id": 1,
                "restrição_medica": "Problema na coluna"
            }
        ]
    }
}

class MembroUpdate(BaseModel):
    nome: str | None = Field(min_length = 2, description="Nome do membro,precisa ter pelo menos duas letras", default=None,examples=["Raul"])
    sobrenome: str | None = Field(min_length = 2, description="Sobrenome do membro, precisa ter pelo menos duas letras", default=None,examples=["Silva"])
    genero: str | None = Field(default=None,min_length = 5, description="Genero do membro, precisa ter pelo menos cinco letras",examples=["Não definido"])
    plano_id: int | None = Field(default=None, description="Identificador do plano na qual a pessoa está matriculada", examples =[1])
    ativo: int | None = Field(default=None, description="0: se o membro não está ativo e 1: se o membro está ativo", examples =[0])
    telefone: str | None = Field(pattern=r'^\d*$', max_length=11,description="O telefone deve ter 11 dígitos DDD+9+número , sem espaços!", default=None)
    email: str | None = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',description="O email deve ser válido", default=None ,examples=["email_normal@gmail.com"])
    personal_id: int | None = Field(default=None,gt=0, description="Colocando o id do personal", examples =[1])
    restricao_medica: str | None = Field(description="Informações sobre restrições médicas a serem seguidas por um membro", examples =["Problema no joelho"], default=None)
    ultima_presenca: date | None = Field(default = None, description="Ultimo dia que o membro frequentou a academia")
    class Config:
        from_attributes = True
        json_schema = model_config_membro_update["json_schema_extra"]

model_config_personal_update = {
    "json_schema_extra": {
        "examples": [
            {
                "membro_id" : [3],
                "telefone" : "88938472651",
                "salario": 2900.0
            }
        ]
    }
}

class PersonalUpdate(BaseModel):
    nome: str | None = Field(min_length = 2, description="Nome precisa ter pelo menos duas letras", default=None, examples=["Roberta"])
    sobrenome: str | None = None
    membro_id: int | None = Field(default=None,description= "Uma lista com os identificadores dos membros da academia que o personal acompanha",examples=[2,3])
    genero: str | None = None
    telefone: str | None = Field(pattern=r'^\d*$', max_length=11,description="O telefone deve ter 11 dígitos DDD+9+número , sem espaços!", default=None)
    email: str | None = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$',description="O email deve ser válido", default=None ,examples=["email_normal2@gmail.com"])
    salario: float | None = Field(gt=0, description="O salário precisa ser maior que zero!", default=None)
    class Config:
        from_attributes = True
        json_schema = model_config_personal_update["json_schema_extra"]

model_config_plano_update = {
    "json_schema_extra": {
        "examples": [
            {
                "preco" : 150.0,
                "promocao" :0
            }
        ]
    }
}

class PlanoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None =  Field(default=None ,description="Mais detalhes sobre o plano",examples=["Plano mais completo com acompanhamento"])
    preco: float | None = Field(default=None,gt=0, description="O preço precisa ser maior que zero!",examples=[100])
    aulas_em_grupo: int | None = Field(default=None, lt=2, description="0: se não oferece aulas em grupo e 1: se oferece aulas em grupo", examples = [0])
    promocao: int | None = Field( default=None,lt=2,description="0: se o plano não está em promoção e 1: se o plano está em promoção",  examples = [1])
    class Config:
        from_attributes = True
        json_schema = model_config_plano_update["json_schema_extra"]





