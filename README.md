# LibraryAPI

Uma simples aplicação Django com Django Rest Framework para criação e manipulação de uma API para uma biblioteca.

## Instalação

- clone o projeto.
- crie um virtualenv em ```library-api/``` .
- ative o virtualenv e instale os requerimentos do projeto.
    
    ```pip install -r requirements.txt```
- entre na pasta ```library``` e crie o banco de dados.

    ```python manage.py migrate```
    
- crie o seu usuário admin.

    ```python manage.py createsuperuser```

- povoe o banco com os dados providos no arquivo ```data.json```.

    ```python manage.py loaddata data```
    
- entre em ```locahost:8000/admin/``` e verifique se foi criado um token para seu usuário. Caso não tenha sido criado, crie um.

## Usagem

- a API funciona para leitura para todo mundo. Porém, se você quiser alterar, excluir ou adicionar algum resgistro, precisa estar prover seu Token na requisição.

- a URL para pegar o token é: ```/api/token/```. Através do seu software preferido (como o postman ou insomnia) envie uma requisição POST com o campo user e password do seu usuário. Você irá receber o token.

- GET - ```/api/books/``` traz todos o livros cadastrados.

- POST - ```/api/books/``` cadastra um novo livro (tem que informar no cabeçalho da requisição a variável ```Authorization: Token meu-token```).

- GET - ```/api/books/<id>/``` traz um livro com id específico.

- PUT - ```/api/books/<id>/``` atualiza todos os campos de um livro.

- PATCH - ```/api/books/<id>/``` atualiza os campos que foram enviados na requisição de um livro (não precisa ser todos os campos do livro).

- DELETE - ```/api/books/<id>/``` delete um livro em específico.
