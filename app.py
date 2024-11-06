# Montando a aplicação com persistencia em bando de dados 

from flask import Flask
from flask_restful import Resource, Api, request
from models import Pessoas, Atividades
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()        #implementação da autenticação
app = Flask(__name__)
api = Api(app)

USUARIOS = {
    'admin':'123'
}


#função chamando a autenticação na logica do codigo
@auth.verify_password
def verificacao(usuario, senha):
    if not (usuario, senha):
        return False
    return USUARIOS.get(usuario) == senha

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            if pessoa is None:
                raise ValueError(f'A pessoa com nome "{nome}" não foi encontrada.')

            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except ValueError as e:
            response = {'status': 'erro', 'mensagem': str(e)}
        except Exception:
            response = {
                'status': 'erro',
                'mensagem': 'Erro desconhecido. Procure o Dev AP administrador da API'
            }
        return response
    @auth.login_required
    def put(self, nome):

        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        if not pessoa:
            return{'status': 'erro', 'mensagem': f'Pessoa com nome "{nome}" não encontrada.'}, 404

        
        if 'nome' in dados:

            pessoa.nome = dados['nome']

        if 'idade' in dados:
            pessoa.idade = dados['idade']

        pessoa.save()

        response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }

        return response
    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        
        if pessoa:
            mensagem_exclusao = f'Exclusão do cadastro de {pessoa.nome} realizada com sucesso.'
            pessoa.deletar() #Aqui esta extraindo o deletar da class Pessoas configurada em models
            return {'status': 'confirmado', 'mensagem': mensagem_exclusao}
        else:
            return {'status': 'erro', 'mensagem': f'Pessoa com nome "{nome}" não encontrada.'}, 404



class ListarPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response
    
    def post(self):
        #mensagem = 'status: cadastro adicionado com sucesso.'
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }

        return response


class ListaAtividades(Resource):
    
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome':i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        

        return response

    def post(self):

        dados = request.json
        pessoa = Pessoas.query.filter_by(nome = dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa = pessoa)
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        atividade.save()
        return response
    

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        
        if pessoa:
            mensagem_exclusao = f'Exclusão do cadastro de {pessoa.nome} realizada com sucesso.'
            pessoa.deletar() #Aqui esta extraindo o deletar da class Pessoas configurada em models
            return {'status': 'confirmado', 'mensagem': mensagem_exclusao}
        else:
            return {'status': 'erro', 'mensagem': f'Pessoa com nome "{nome}" não encontrada.'}, 404
        
    def put(self, id):
        dados = request.json
        atividade = Atividades.query.get(id)

        if not atividade:
            return {'status': 'erro', 'mensagem': f'Atividade com id "{id}" não encontrada.'}, 404

        if 'nome' in dados:
            atividade.nome = dados['nome']
        if 'pessoa' in dados:
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            if pessoa:
                atividade.pessoa = pessoa
            else:
                return {'status': 'erro', 'mensagem': f'Pessoa com nome "{dados["pessoa"]}" não encontrada.'}, 404

        atividade.save()
        response = {
            'id': atividade.id,
            'nome': atividade.nome,
            'pessoa': atividade.pessoa.nome
        }
        return response, 200

# Adicionando a rota do endpoint
api.add_resource(Pessoa, '/pessoa/<string:nome>/', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(ListarPessoas, '/listapessoas/', methods = ['GET', 'PUT', 'POST', 'DELETE'])
# Adicionando a rota do endpoint para ListaAtividades com 'id'
# Adicionando rotas do endpoint para ListaAtividades com endpoints diferentes
api.add_resource(ListaAtividades, '/atividades/', endpoint='lista_atividades')
api.add_resource(ListaAtividades, '/atividades/<int:id>/', endpoint='atividade_unica')

if __name__ == '__main__':
    app.run(debug=True)

