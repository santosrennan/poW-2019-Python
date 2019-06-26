Como instalar?

1-Tenha o python em seu computador
2- Baixe o Anaconda que cria envs... pode ser utilizado o virtualenv.
3- crie uma env no conda ou virtualenv passando a versão do python 3.5
4-  abra sua env e instale os requirements
5- Certifique que todas as dependencias do requirements foram feitas
6 - De cd até achar o manage.py  alocado em gamestore
6- Faça um python migrate
7 -  Faça um python runserver
8 - Abra localhost:8000


Comandos de auxilio

1 - conda create --name myenv python==3.5
2 - conda activate myenv
3-  pip install -r requirements
4-  python manage.py migrate
5 - python manage.py runserver


É importante que a configuração seja bem realizada para rodar todas dependencias do django e do python.
Criação de Env é imporante para que as dependencias do projeto não de conflito com as dependencias possiveis que já estejam na maquina.
