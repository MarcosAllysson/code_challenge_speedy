# Python Challenge 20200228

## Introdução

Nesse desafio trabalharemos no desenvolvimento de uma REST API para utilizar os dados do projeto Open Food Facts, que é um banco de dados aberto com informação nutricional de diversos produtos alimentícios.

O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que eles possam revisar de maneira rápida a informação nutricional dos alimentos que os usuários enviam pela aplicação móvel.

[SPOILER] As instruções de entrega e apresentação do challenge estão no final deste Readme (=

### Obrigatório
 
- Trabalhar em um FORK deste repositório em seu usuário ou fazer em seu github pessoal;
- O projeto back-end deverá ser desenvolvido usando Python com [FastAPI](https://fastapi.tiangolo.com/) ou [Django Rest Framework](https://www.django-rest-framework.org);
- Configurar os testes usando Pytest ou algum de sua preferência;
- Documentação para configuração do projeto em ambientes de produção (como instalar, rodar e referências a libs usadas);
 

## O projeto
 
- Criar um banco de dados MongoDB usando Atlas: https://www.mongodb.com/cloud/atlas ou algum Banco de Dados SQL se não sentir confortável com NoSQL;
- Criar uma REST API usando Django Rest Framework ou FastAPI com as melhores práticas de desenvolvimento
- Integrar a API com o banco de dados criado para persistir os dados
- Recomendável usar Drivers oficiais para integração com o DB
- Desenvolver Testes Unitários

### Modelo de Dados:

Para a definição do modelo, consultar o arquivo [products.json](./products.json) que foi exportado do Open Food Facts, um detalhe importante é que temos dois campos personalizados para poder fazer o controle interno do sistema e que deverão ser aplicados em todos os alimentos no momento da importação, os campos são:

- `imported_t`: campo do tipo Date com a dia e hora que foi importado;
- `status`: campo do tipo Enum com os possíveis valores draft, trash e published;

### Sistema do CRON

Para prosseguir com o desafio, precisaremos criar na API um sistema de atualização que vai importar os dados para MongoDB com a versão mais recente do [Open Food Facts](https://br.openfoodfacts.org/data) uma vez ao día. Adicionar aos arquivos de configuração o melhor horário para executar a importação.

A lista de arquivos do Open Food, pode ser encontrada em: 

- https://challenges.coode.sh/food/data/json/index.txt
- https://challenges.coode.sh/food/data/json/data-fields.txt

Onde cada linha representa um arquivo que está disponível em https://challenges.coode.sh/food/data/json/{filename}. O nome do arquivo contém o timestamp UNIX da primeira e última alteração contida no arquivo JSON, para que os arquivos possam ser importados (após extracção) em ordem alfabética.

É recomendável utilizar uma Collection secundária para controlar os históricos das importações e facilitar a validação durante a execução.

Ter em conta que:

- Todos os produtos deverão ter os campos personalizados `imported_t` e `status`.
- Limitar a importação a somente 100 produtos de cada arquivo.

### A REST API

Na REST API teremos um CRUD com os seguintes endpoints:

 - `GET /`: Detalhes da API, se conexão leitura e escritura com a base de dados está OK, horário da última vez que o CRON foi executado, tempo online e uso de memória.
 - `PUT /products/:code`: Será responsável por receber atualizações do Projeto Web
 - `DELETE /products/:code`: Mudar o status do produto para `trash`
 - `GET /products/:code`: Obter a informação somente de um produto da base de dados
 - `GET /products`: Listar todos os produtos da base de dados, adicionar sistema de paginação para não sobrecarregar o `REQUEST`.

Ao terminar os endpoints, configurar os testes usando Pytest ou algum de sua preferência.


## [Bônus] DevOps

Depois de um árduo trabalho de desenvolvimento na API chegou a hora mais esperada, 
o lançamento do projeto, é uma das partes mais motivadoras verdade? Então, a equipe de administração de 
sistemas precisará dos mínimos detalhes para configurar o projeto em produção, 
por isso é sua responsabilidade documentar todo o fluxo e facilitar a configuração dos dois projetos com 
tecnologias chaves para rodar em ambientes de Cloud Computing. 

Para isso deveremos configurar:

- Dockerfile
- Docker compose para executar o projeto em ambiente local


## Readme do Repositório

- Deve conter o título do projeto
- Uma descrição sobre o projeto em frase
- Deve conter uma lista com linguagem, framework e/ou tecnologias usadas
- Como instalar e usar o projeto (instruções)
- Não esqueça o [.gitignore](https://www.toptal.com/developers/gitignore)
- Se está usando github pessoal, referencie que é um challenge by coodesh 

## Finalização e Instruções para a Apresentação

Avisar sobre a finalização e enviar para correção.

1. Confira se respondeu o Scorecard Python Developer ou candidatou-se em uma vaga (dúvidas: contato@coodesh.com);
2. Verique se o Readme está bom e faça o commit final em seu repositório;
3. Acesse: [https://coodesh.com/review-challenge](https://coodesh.com/review-challenge);
4. Coloque seu nome completo; 
5. Coloque seu e-mail;
6. Adicione o repositório com a sua solução;
7. Confira a vaga desejada;

![Solicitar Correção](https://res.cloudinary.com/coodesh/image/upload/v1612571243/coodesh-teams/challenges/repo.gif)

8. Envie e aguarde as instruções para apresentação da sua solução

## Instruções para se preparar para a Apresentação:

1. Aguarde o e-mail com as instruções de apresentação 
2. Enquanto isso, crie uma conta na plataforma: https://www.loom.com/ e instale o Desktop App ou Extensão no Chrome: https://www.loom.com/download 
3. DICA: Será necessário compartilhar a tela durante a gravação ou vídeo chamada. Deixe todos os projetos de solução previamente abertos em seu computador antes de iniciar a gravação ou chamanda de vídeo. Ambientes configurados e prontos para rodar.
4. Prepara-se pois você será questionado sobre cada etapa e decisão do Challenge. Prepare uma lista de perguntas, dúvidas, sugestões de melhorias e feedbacks (caso tenha).

## Suporte

Use o nosso canal no slack: http://bit.ly/32CuOMy para tirar dúvidas sobre o processo ou envie um e-mail para contato@coodesh.com.

