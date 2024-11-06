#criando a inserção e consulta de dados:

from models import Pessoas, Usuarios

def inserir_pessoas():
    #campo de teste para verificar se está inserindo e contultando:
    pessoa = Pessoas(nome= 'PQD', idade= 41)
    print(pessoa)
    pessoa.save()

def consultar():

    pessoa = Pessoas.query.all()
    #poderia ser assim:  #idades = Pessoas.query.with_entities(Pessoas.idade).all() / print(idades)
    print(pessoa) 

def alterar_pessoas():

    pessoa = Pessoas.query.filter_by(nome='Albino').first()
    pessoa.nome = 'PQD'
    pessoa.save

def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='PQD').first()
    if pessoa:
        pessoa.deletar()  # Chama o método deletar diretamente na instância, ajuste da aula.

def insere_usuario(login, senha):                       #insere usuarios na estrutura da tabela Usuarios
    usuario = Usuarios(login = login, senha = senha)
    usuario.save()

def consulta_todos_usuarios():                          #consulta os usuarios cadastrados na tabela Usuarios
    usuarios = Usuarios.query.all()
    print(usuarios)                 #aqui é para verificar se essa logica funciona dando output no terminal com users inseridos



if __name__ == '__main__':
    insere_usuario('albino', '1234')
    insere_usuario('ferreira', '4321')
    consulta_todos_usuarios()
    #excluir_pessoas()
    #alterar_pessoas()
    #inserir_pessoas()
    #consultar()