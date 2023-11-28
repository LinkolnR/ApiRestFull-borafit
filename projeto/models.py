from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
'''
Os models desse arquivo são os do SqlAlchemy,
não confundir com os do Pydantic, que estarão no schema.py
'''
### COLOCAR OS EXEMPLOS AINDA POR CONTA DA documentação
class Membro(Base):
    __tablename__ = 'membros'  # Nome da tabela no banco de dados

    membro_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(50))
    genero = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    plano_id = Column(Integer, ForeignKey('plano.plano_id'), nullable=False)
    ativo = Column(Integer, nullable=False)
    telefone = Column(String(11))
    email = Column(String(100), nullable=False, unique=True)
    personal_id = Column(Integer, ForeignKey('personal.personal_id'))
    restricao_medica = Column(String(100), default="nenhuma")
    data_inscricao = Column(Date, default=datetime.now().date(), nullable=False)
    ultima_presenca = Column(Date)

    # Define relationships if needed
    plano = relationship("Plano", back_populates="membros")
    personal = relationship("Personal", back_populates="membros")

    


class Plano(Base):
    __tablename__ = 'plano'

    plano_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), index=True, nullable=False)
    descricao = Column(String(50), index=True)
    preco = Column(Float, nullable=False)
    aulas_em_grupo = Column(Integer, default=0, nullable=False)
    promocao = Column(Boolean, default=False, nullable=False)

    membros = relationship("Membro", back_populates="plano")


class Personal(Base):
    __tablename__ = 'personal'

    personal_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(50), nullable=False)
    membro_id = Column(Integer )  # You can use a JSON or array type field in your database, depending on the database you are using
    cpf = Column(String(11), nullable=False, unique=True)
    genero = Column(String(50), nullable=False)
    telefone = Column(String(11), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    salario = Column(Float, nullable=False)
    membros = relationship("Membro", back_populates="personal")

