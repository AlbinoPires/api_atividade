#criando a inserção e consulta de dados:

from models import Pessoas

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



if __name__ == '__main__':
    excluir_pessoas()
    #alterar_pessoas()
    #inserir_pessoas()
    consultar()