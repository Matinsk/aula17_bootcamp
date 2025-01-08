from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo = True)
URI = "postgresql+pyodbc://dbuser:kx%40jj5%2Fg@pghost10/appdb"


print('Conexão com SQLite estabelecida')


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)


Base.metadata.create_all(engine)