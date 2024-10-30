# Aula para manipulação com SQLAlchemy e SQLite:

# Importa as ferramentas necessárias do SQLAlchemy para criar a engine e manipular sessões de banco de dados
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base


# Cria uma "engine" que é a interface de conexão com o banco de dados SQLite.
# Aqui, 'sqlite:///atividades.db' cria um banco de dados chamado "atividades.db" no mesmo diretório do projeto.
# O parâmetro convert_unicode=True garante que o SQLAlchemy trate os dados como Unicode,
# permitindo armazenamento adequado de caracteres especiais.
engine = create_engine('sqlite:///atividades.db')

# Configura a sessão de banco de dados:
# A função sessionmaker cria uma fábrica de sessões, e o scoped_session faz o gerenciamento automático da sessão,
# especialmente útil em aplicativos de múltiplas threads.
# O autocommit=False desativa o autocommit, para que as transações só sejam salvas ao chamar "commit()".
# O parâmetro bind=engine conecta essa sessão ao banco de dados especificado pela engine.
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Define uma classe base a partir da qual as classes de modelo serão criadas.
# "declarative_base()" cria uma classe base que será usada para definir as tabelas.
Base = declarative_base()

# Adiciona a propriedade `query` a todas as classes derivadas de Base,
# permitindo realizar consultas de forma mais conveniente usando `Classe.query`.
# `query_property()` faz com que `query` seja automaticamente associado à sessão `db_session`.
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoas(nome={self.nome}, idade={self.idade})>'
        #correção do original pois em aula explicitamos somente nome, no teste output no terminal
    #método para commitar() sendo chamado em utils, chamamdo pessoa.save()
    def save(self):
        db_session.add(self)
        db_session.commit()

    def deletar(self):
        db_session.delete(self)
        db_session.commit()
        

class Atividades(Base):

    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")




def init_db():
    Base.metadata.create_all(bind=engine)




if __name__ == '__main__':
    init_db()