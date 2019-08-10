# ProyectoGuiarConsultores

**Contenidos**
1. [Clonar Proyecto](#gitClone)
2. [Instalar Python 3.X](#pythonInstall)
3. [Instalar Django](#djangoInstall)
4. [Instalacion de MySQL 8.0.17](#mysqlInstall)
5. [Instalar mysqlclient](#mysqlclientInstall)
6. [Crear Base de datos para GuiarConsultores](#createDatabase)
7. [Configurar ProyectoGuiarConsultores con MySQL 8.0.17](#configDatabase)
8. [Crear tablas en Django](#createTables)
9. [MakeMigrations](#makemigrations)
10. [Migrations](#migrate)
11. [Levantar Servidor](#runserver)

<a name="gitClone"></a>
## Clonar ProyectoGuiarConsultores
Para continuar el desarrollo del sistema en otro equipo, usted debe clonar el proyecto a través de github mediante la consola de windows ejecutar el siguiente instruccion (verifique que se encuentre en el directorio deseado):
  ```
  git clone https://github.com/JulioCesar0180/ProyectoGuiarConsultores.git
  ```

<a name="pythonInstall"></a>
## Instalar python 3.X
Se requiere instalar python 3.6 (min version) de 64 bits.

<a name="djangoInstall"></a>
## Instalar Django
Se requiere instalar Django ejecutando la siguiente instruccion:
```
py -m pip install Django
```

<a name="mysqlInstall"></a>
## Instalacion de MySQL 8.0.17
Instalar los prodcutos de MySQL 8.0.17 desde el siguiente link: https://dev.mysql.com/downloads/file/?id=488055
  - MySQL Server
  - MySQL Workbench
  - Connector/Python (3.6) 8.0.17
  - El resto de los productos es opcional
  
  Nota: Al finalizar la instalacion de MySQL, puedes ejecutar MySQL Installer para instalar un producto que hayas olvidado, de esta manera evitas la reinstalacion.

<a name="mysqlclientInstall"></a>
## Instalar mysqlclient
1. Ejecutar la siguiente instruccion en la consola de comandos de windows (la ubicacion dependera en que ambiente de desarrollo tiene instalado python)
```
py -m pip list
```
2. Se desplegará un listado de todos los modulos instalados en su equipo
3. Desinstalar el paquete **pymysql** si lo tiene instalado, ejecute la siguiente instruccion:
```
py -m pip uninstall pymysql
```
3. En el listado del paso N°2, ubique el paquete **mysqlclient 1.4.2.post1**. (las versiones posteriores a esta tambien son compatibles)
4. En caso que no tenerlo instalado, ejecutar la siguiente instruccion:
```
py -m pip install mysqlclient
```
5. En caso de tener una version no compatible, ejecutar la siguiente instruccion para actualizar:
```
py -m pip install --upgrade mysqlclient
```

<a name="createDatabase"></a>
## Crear la Base de Datos para GuiarConsultores
2. En MySQL Workbench ingresamos a nuestra base de datos local (localhost) y escribimos la siguiente query:
```sql
CREATE DATABASE guiarconsultores CHARACTER SET utf8mb4;
```
3. Crear un usuario y asignarle todos los previlegios para la administracion de la base de datos
  * user: admin
  * password: root
```sql
CREATE USER admin@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON guiarconsultores.* TO admin@localhost;
FLUSH PRIVILEGES;
```

<a name="configDatabase"></a>
## Configurar ProyectoGuiarConsultores con MySQL 8.0.17
En el archivo **settings.py** de la carpeta ProyectoGuiarConsultores
```
ProyectoGuiarConsultores/
    manage.py
    .gitignore
    db.sqlite3
    ProyectoGuiarConsultores/
        __init__.py
        settings.py       <--- Este archivo
        urls.py
        wsgi.py
    Home/
    Poll/
```
En el archivo mencionado anteriormente debemos ubicar el diccionario ```DATABASES``` y configurarlo de la siguiente manera:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guiarconsultores',
        'USER': 'admin',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

<a name="createTables"></a>
## Crear tablas en Django
El archivo **models.py** es encargado de construir una tabla en la base de datos. Cada aplicacion tiene su propio archivo **models.py** y en este caso vamos a crear la tabla ```Tabla_usuario```
```python
from django.db import models

# Create your models here.

class Tabla_usuario(models.Model):
    user = models.CharField(max_length=200)
    pass_user = models.CharField(max_length=200)
```
Lo anterior muestra el codigo insertado en el archivo models.py de la aplicacion Poll.

<a name="makemigrations"></a>
## MakeMigrations
Para crear las migraciones es necesario ejecutar la siguiente instruccion en la consola de windows (Es obligatorio ejecutar esta instruccion donde se encuentra almacenado el ProyectoGuiarConsultores)
```
py manage.py makemigrations
```

<a name="migrate"></a>
## Migrations
Para migrar las tablas es necesario ejecutar la siguiente instruccion en la consola de windows (Es obligatorio ejecutar esta instruccion donde se encuentra almacenado el ProyectoGuiarConsultores)
```
py manage.py migrate
```

<a name="runserver"></a>
## Levantar Servidor
Para visualizar la pagina web se debe ejecutar la siguiente instruccion en la consola de windows (Es obligatorio ejecutar esta instruccion donde se encuentra almacenado el ProyectoGuiarConsultores)
```
py manage.py runserver
```
