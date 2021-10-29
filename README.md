# Code Chagellend Speedy - Python Developer
Challenge by coodesh.

- Nesse desafio foi desenvolvido uma REST API para utilizar os dados do projeto Open Food Facts.
- O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que eles possam 
revisar de maneira rápida a informação nutricional dos alimentos que os usuários enviam pela aplicação móvel.

## Tecnologias
- Django/Django Rest Framework
- Docker/Docker-compose
- Postgre
- Pytest
- Python

## Como rodar o projeto
- Clone este repositório
- Execute: ```docker-compose build```
- Execute: ```docker-compose up```

## Endpoints
- "Products":
  * -- PUT: http://127.0.0.1:8000/api/v1/products/:id/
  * -- DELETE: http://127.0.0.1:8000/api/v1/products/:id/
  * -- GET PRODUCT: http://127.0.0.1:8000/api/v1/products/:id/
  * -- GET PRODUCTS: http://127.0.0.1:8000/api/v1/products/
  * -- POST: http://127.0.0.1:8000/api/v1/products/
- "API":
  * -- GET: http://127.0.0.1:8000/api/v1/

## Testando API
- Execute: ```docker-compose exec backend pytest productsapp/tests/test_product.py```
- Execute: ```docker-compose exec backend pytest productsimportationapp/tests/test_product.py```

## Acesse Django's admin
- http://127.0.0.1:8000/admin/

### Observações
- A parte do cron, foi feito somente a importação do json via link. Por problemas técnicos, não foi possível importar
os dados para o banco. Visto que tamanho do arquivo a máquina teve dificuldade até para ler o arquivo. Entretanto, 
a função que faz importação foi parcialmente implementada e usando apenas o primeiro arquivo .gz.
- Gostei do projeto, serviu de bastante aprendizado e me mantenho aberto a qualquer feedback.
