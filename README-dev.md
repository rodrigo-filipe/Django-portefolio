# Django-portefolio
Progeto para portefolio

--- 


## Como executar
1 - Abrir o cmd

2 - Dirigir-se á pasta do projeto

3 - Entrar no venv (virtual enviroment)

```
source venv/bin/activate
```

Sabe que o comando correu bem quando aparece (venv) antes da pasta onde está a trabalhar

```
(venv) C:\Users\PC\Desktop\meu_portefolio>
```

4- Depois disso deve correr o server em localHost

```
python manage.py runserver
```

Deverá aparecer uma mensagem deste genero:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 11, 2026 - 21:20:13
Django version 5.2.13, using settings 'portefolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

De seguida pode aceder ao site escrevendo na barra de pesquisa 

```
http://127.0.0.1:8000/
```

Se quiser entrar no painel de admin é só escrever:

```
http://127.0.0.1:8000/admin
```
---

## Alterações ao models:

Após qualquer alteração do models deve se fazer os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
```

---


