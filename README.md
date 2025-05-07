# Sistema de Adoção de Animais

Sistema para auxiliar o controle e gestão para as organizações que fazem a adoção de animais de estimação ou que necessitem de uma plataforma para o registro de seu catalogo de animais.

### 👉 [CI/CD Build Status](http://127.0.0.1:8080/job/pet_adoption_manager/)
> Seguimos um fluxo de trabalho de integração contínua para manter a qualidade do código. Para mais detalhes sobre os processos automatizados de build e teste, confira o link do [Jenkins](http://127.0.0.1:8080/job/pet_adoption_manager/).

### 👉 [Log da Aplicação](http://127.0.0.1:9009)
> Este link te direcionará para a interface de visualização dos logs de todos os containers das aplicações.

# Sumário
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#prerequisitos)
- [Iniciar a aplicação no Docker](#rundocker)
- [Como iniciar a aplicação](#runproject)
- [Como executar os testes](#runtests)
- [Documentação](#documentation)
- [Contribuindo com o Projeto](#contributing)

<br />

## 📜 Funcionalidades <a name="funcionalidades"></a>
> Principais serviços disponiveis no sistema:
- Cadastro de Animais e Características:
    - Permite o registro detalhado de animais, incluindo informações como nome, idade, raça, sexo, cor, e qualquer outra característica relevante. Este serviço facilita a gestão eficiente do inventário de animais disponíveis para adoção, garantindo que todas as informações necessárias estejam facilmente acessíveis.
- Cadastro de Vacinas:
    - Facilita o registro e acompanhamento das vacinas aplicadas aos animais. Este serviço é crucial para garantir que os animais estejam sempre protegidos contra doenças, melhorando sua saúde e bem-estar.
- Auditoria de Alterações e Inserções de Dados:
    - Implementa um sistema de auditoria que rastreia todas as alterações e inserções de dados realizadas no sistema. Isso inclui informações sobre quem fez a alteração, quando foi feita, e quais dados foram modificados. Este serviço é essencial para garantir a integridade e a segurança dos dados, permitindo a identificação e correção de erros, além de fornecer um histórico completo das atividades realizadas no sistema.
- Gestão de Usuários e Permissões:
    - Permite a criação, edição e exclusão de perfis de usuário, além de definir permissões e níveis de acesso. Este serviço garante que apenas usuários autorizados possam realizar determinadas ações, aumentando a segurança e a confiança no sistema.
- Relatórios e Análises:
    - Oferece a geração de relatórios detalhados e análises sobre diversos aspectos do sistema, como o número de animais adotados, vacinas aplicadas, e atividades de auditoria. Esses relatórios são essenciais para a tomada de decisões informadas e para a avaliação do desempenho das organizações de doação de animais.

## 💻 Pré-requisitos <a name="prerequisitos"></a>

> Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a versão mais recente do `docker` e `docker-compose`.
* Você instalou a versão `3.9` do `python`.
* Você tem uma máquina `Windows` ou `Linux`.
* Você tem o arquivo `.env` com as credencias utilizadas pelo sistema
* Você leu os guias de `Iniciar a aplicação no Docker` e `Como usá-lo`.

<br />

## ✨ Iniciar a aplicação no Docker <a name="rundocker"></a>

> **Parte 1** - Baixe o código do repositório (usando o `GIT`) 
```bash
$ git clone https://github.com/ViniciusCruzMoura/pet_adoption_manager.git
$ cd pet_adoption_manager
```

<br />

> **Parte 2** - Iniciar a aplicação no `Docker`
```bash
$ docker-compose up --build 
```

Visite `http://localhost:9090` em seu navegador. A aplicação deve estar configurada e rodando.
#### Usuario Padrão, Login: admin Senha: admin

<br />


## ✨ Como iniciar a aplicação <a name="runproject"></a>

> Baixe o código 
```bash
$ git clone https://github.com/ViniciusCruzMoura/pet_adoption_manager.git
$ cd pet_adoption_manager
```

<br />

### 👉 Configurar para `Linux`

> Instalar as dependências via `VENV`  
```bash
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Configurar o banco de dados
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

<br />

> Iniciar a aplicação
```bash
$ python3 manage.py runserver
```

Neste ponto, a aplicação é acessível em `http://127.0.0.1:8000/`. 
#### Usuario Padrão, Login: admin Senha: admin

<br />

### 👉 Configurar para `Windows` 

> Instalar as dependências via `VENV` (windows) 
```
$ python -m vevn env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> Configurar o banco de dados
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Iniciar a aplicação
```bash
$ python manage.py runserver
```

Neste ponto, a aplicação é acessível em `http://127.0.0.1:8000/`. 
#### Usuario Padrão, Login: admin Senha: admin

<br />

## 📋 Como executar os testes <a name="runtests"></a>

> É necessário instalar as dependências(requirements.txt), e configurar as variáveis de ambiente(.env)
```bash
# Testes de Unidade
$ python -m unittest discover tests/unit/
# Testes de Integração
$ python -m unittest discover tests/integration/
# Todos os testes
$ python -m unittest discover tests/
# Executar com o Docker
$ docker compose run --rm --build web sh -c "python -m unittest discover tests/"
```
<br />

## 📚 Documentação <a name="documentation"></a>
- [API Documentação](docs/)
- [Guia](docs/)
- [Licença](#license)
<br />

## 📫 Contribuindo com o Projeto <a name="contributing"></a>
> Para contribuir com o projeto, siga estas etapas:

1. Faça o fork deste repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

<br />

