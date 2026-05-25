# Repositorio de Programación Orientada a Objetos con Python
Repositorio con ejercicios de Programación Orientada a Objetos


## 1. Crear .gitignore

Crear el arhivo .gitignore para configurar los archivo sy carpeta que no deseamos que se guarden en el repositorio

````shell
*.pyc
_pycache_/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos nuevos.

````shell
git add . 
````

## 3. Crear un COMMIT

Crear un commit o puento de control de los cambios realizados en el proyecto.

````shell
git commit -m "CREATED .gitignore"
````

* CREATED - Se crearon nuevas carpetas o archivos.
* UPDATED - Se actualizaron o agregaron nuevas funciones.
* FIXED - Se corriegieron errores.


## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio.

````shell
git push -u origin main
````

## 5. Agregar Documentación a los métodos

Agregar un  **Docstring** a los métodos generados.

´´´´Python
def metodo(self):
"""
Se describe el método.

Args: (Argumentos)
Se describen los argumentos.
Return:
Se describen lo que regresa el return.
