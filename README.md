# n-queens-puzzle
n queens puzzle

## Introduccion

Este repositorio contiene una "command-line app" escrito en python para 
resolver el problema de las n reinas:

[https://en.wikipedia.org/wiki/Eight_queens_puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle)

La implementacion para resolver el problema se llama "Bit Magic"
El articulo de donde fue extraido el algoritmo es:

[https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/](https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/)

El codigo fuente del algoritmo del articulo esta un repositorio de GitHub:

[https://github.com/edorado93/Save-The-Queens/tree/master](https://github.com/edorado93/Save-The-Queens/tree/master)

- La aplicacion itera sobre las soluciones a un tablero de N por N, de una propuesta,
- Guarda las soluciones en una base de datos (postgres)
- Cuenta con un test para verificar el numero de soluciones arrojados por la aplicacion
- La aplicacion fue Dockerizada
- Tiene el setup necesario para correr las pruevas al momento de integrar cambios (Travis CI)

## Requerimientos

la aplicacion fue dockerizada asi que no necesitas nada mas que:
- Docker [docker version 19.03.2](https://docs.docker.com/engine/release-notes/#19032)
- Docker Compose [docker-compose version 1.24.1](https://docs.docker.com/release-notes/docker-compose/#1241)

* no existe preocupacion por la version de python o posgres docker esta aqui para salvarnos

## Correr el contenedor

```
$ # clona el repositorio
$ git clone https://github.com/gAmadorH/n-queens-puzzle.git
$ # cambiate de directorio
$ cd n-queens-puzzle/
# interactua con la aplicacion, ejecutando un comando
$ docker-compose run puzzle python index.py
```

Es posible que tengas problemas si ya estas usando el puero 5432 para una base de datos

si lo deseas puedes comprobar que la base de datos existe, puedes ingresar con un cliente grafico de base de datos en el siguiente url

`postgresql://nQueensPuzzle:nQueensPuzzle@localhost:5432/nQueensPuzzle`

## detener el contenedor

```
$ # Solo debes precionar la tecla Enter para salir de la aplicacion
$ # despues hacer down del contenedor
$ docker-compose down
```

## Correr las pruebas en el contenedor

```
$ # tambien puedes correr las las pruebas si lo deseas
$ docker-compose run puzzle pytest -v
```