# Sistema de Gestão para Adoção de Animais (protótipo)

## ✨ Iniciar a aplicação no Docker

> **Parte 1** - Baixe o código do repositório (usando o `GIT`) 
```bash
$ git clone https://github.com/ViniciusEduardoCruzMoura/prototype_2.git
$ cd prototype_2
```

<br />

> **Parte 2** - Iniciar a aplicação no `Docker`
```bash
$ docker-compose up --build 
```

Visite `http://localhost:5085` em seu navegador. A aplicação deve estar configurada e rodando.

<br />


## ✨ Como usá-lo

> Baixe o código 
```bash
$ git clone https://github.com/ViniciusEduardoCruzMoura/prototype_2.git
$ cd prototype_2
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