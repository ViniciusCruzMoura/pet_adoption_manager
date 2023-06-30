# Sistema de Adoção de Animais

Sistema para auxiliar o controle e gestão para as organizações que fazem a adoção de animais de estimação ou que necessitem de uma plataforma para o registro de seu catalogo de animais.

<br />

## 💻 Pré-requisitos

> Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a versão mais recente do `docker` e `docker-compose`.
* Você instalou a versão `3.9` do `python`.
* Você tem uma máquina `Windows` ou `Linux`.
* Você tem o arquivo `.env` com as credencias utilizadas pelo sistema
* Você leu os guias de `Iniciar a aplicação no Docker` e `Como usá-lo`.

<br />

## ✨ Iniciar a aplicação no Docker

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

<br />


## ✨ Como usá-lo

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

<br />

## 📫 Contribuindo com o Projeto
> Para contribuir com o projeto, siga estas etapas:

1. Faça o fork deste repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

<br />

