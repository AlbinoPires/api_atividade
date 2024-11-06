# 👋 Olá, eu sou Albino Pires!

🌐 **Cloud Enthusiast | AWS Cloud | Python | Linux | Flask**

---

# SECURITY.md

## 🛡️ Segurança e Autenticação para a API

Este documento aborda o uso de autenticação básica para proteger endpoints específicos de nossa API em Flask usando `flask-httpauth`. O objetivo é garantir que somente usuários autorizados possam acessar ou modificar dados sensíveis, protegendo-os contra acessos não autorizados.

### 🚀 Instalação e Configuração do Flask-HTTPAuth

1. **Setup Utilizado**:
    - Ubuntu | VSCode | Postman | Browser Mozila | Flask-httpauth

2. **Instalação do Flask-HTTPAuth**:
   - Certifique-se de estar no ambiente virtual do projeto e instale a biblioteca usando:
     ```bash
     pip install Flask-HTTPAuth
     ```

3. **Implementação do Autenticador**:
   - No código de `app.py`, configuramos uma função para verificar o login do usuário e restringir o acesso aos endpoints que requerem autenticação. Esta verificação é feita com `@auth.login_required` no endpoint que queremos proteger.
   
4. **Configuração do Usuário e Senha**:
   - Definimos um dicionário de usuários e senhas (pode ser ajustado para métodos mais seguros em produção) e adicionamos uma função para verificar as credenciais:
     ```python
     USUARIOS = {
         'admin': '321'
     }
     ```

5. **Exemplo de Proteção em Endpoints**:
   - Somente o endpoint `/listapessoas/` exige autenticação, enquanto os demais seguem livres para fins de teste. Este comportamento reflete o uso do decorator `@auth.login_required` na classe `ListarPessoas`.

6. **Exemplo de Teste da Autenticação no Navegador**:
   - Abaixo está um exemplo de autenticação bem-sucedida no navegador (consulte a imagem `security.png`):
   
     ![Print do Teste de Autenticação](./security.png)

### 🔒 Comportamento e Observações

- Ao autenticar-se em um endpoint, o navegador tende a "lembrar" a sessão, permitindo que os demais endpoints possam ser acessados sem nova solicitação de senha. Esse comportamento padrão do `flask-httpauth` facilita o uso contínuo da API sem a necessidade de autenticações repetidas durante a mesma sessão.
  
- Este é um comportamento importante para testes de desenvolvimento e pequenas APIs. Porém, em produção, o ideal é que autenticações mais fortes, como tokens JWT, sejam consideradas.

### ✅ Considerações Finais

O uso de autenticação básica com `flask-httpauth` é uma excelente introdução ao controle de acesso para APIs RESTful. No entanto, é fundamental ter em mente que, em projetos de maior escala ou em produção, outras formas de autenticação mais robustas são recomendadas. 

**Recomendações para Autenticações Futuras**:
- **Autenticação JWT (JSON Web Token)**: Mais segura para aplicações que exigem persistência de sessão e maior controle de expiração.
- **OAuth**: Amplamente utilizado para autenticações em APIs, permitindo o uso de contas de terceiros (Google, GitHub) com segurança.
- **Kubernetes Secrets**: Ferramenta de segurança adicional para proteger credenciais de forma centralizada em ambientes Kubernetes.

### 📈 Lições Aprendidas

Com a implementação desta autenticação básica, foi possível aprender:
- A estrutura básica de controle de acesso em Flask.
- A vantagem de aplicar autenticação em endpoints específicos.
- A importância de explorar opções mais avançadas de autenticação conforme o projeto cresce.

--- 
