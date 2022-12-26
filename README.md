# Prueba Tecnica - Desarrollador Backend SFA

Este proyecto tiene como objetivo implementar un API Rest en Django de un sistema de información que permita registrar los datos de votantes de las diferentes ciudades o municipios. Para este sistema se tendrán dos roles principales que tendrán acceso al sistema, mediante un login que devuelve un token permitiendo con este consultar los diferentes servicios del sistema. Para este desarrollos de planteo el siguiente diagrama entidad relación:

![PruebaTecnica drawio (1)](https://user-images.githubusercontent.com/62753088/209579482-c712d441-c3f0-4d95-be48-8a25632562ee.png)

En la cual vemos las tablas:
1.	Django User
  - Esta tabla es generada por Django, teniendo un objetivo importante para el registro de usuarios.
    - Este sistema ofrece un CRUD de esta tabla.
2.	Leader
  -	Esta tabla es para el rol de lider el cual tiene relación con la tabla User Django debido a que nos permite autenticar y loguear el usuario.
    - Este sistema ofrece un CRUD de esta tabla.
3.	Voter
  - Esta table es el votante que será registrado, este no tiene relación con la tabla User Django debido a que este rol no tendrá ningún acceso al sistema.
    - Este sistema ofrece un CRUD de esta tabla.
4.	Department
  - Esta tabla es para los departamentos.
    - Este sistema ofrece un CRUD de esta tabla.
5.	City
  - Esta tabla es para las ciudades que se encuentran en cada departamento.
    - Este sistema ofrece un CRUD de esta tabla.
6.	Neighborhood
  - Esta tabla es para los barrios.
    - Este sistema ofrece un CRUD de esta tabla.
7.	Polling Place
  - Esta tabla es para los lugares de votación.
    - Este sistema ofrece un CRUD de esta tabla.
8.	Log
  - Esta tabla es log que guardara toda la trazabilidad de los voter, a ser actualizados o creados por los lideres.
    - Este sistema ofrece un CRUD de esta tabla.
9.	Type Log
  - Esta tabla son los tipos de log.
    - Este table no cuenta con crud, debido a que será una tabla estatica.
10.	Document Type
  - Esta tabla es para los tipos de documento de identificación.
    - Este sistema ofrece un CRUD de esta tabla.


## Tener en cuenta que:
Para todas las tablas que cuentan con un CRUD en el sistema, el método DELETE no se realiza, esto con el fin de evitar la pérdida de la integridad referencial.

## Instalación
1. Para la instalación y ejecución del sistema, se deben tener con:

- Tener instalado alguna versión de Python 3.
- Tener base de datos PostgreSQL (importar la base de datos)

2. Al tener instalados Python y PostgreSQL, se continua con la configuración de un entorno virtual en el que se puedan instalar las dependencias, sin afectar las dependencias locales del equipo.

- Para más información sobre los entornos virtuales visitar [Entornos Virtuales - Guía](https://docs.python.org/es/3/tutorial/venv.html)

3. Instalar las dependencias. En este repositorio se encuentro el archivo "requirements.txt" donde se listan todas las dependencias que se usaron en el proyecto. En la consola estando activo el entorno virtual, ejecutamos el siguiente comando:

  ```
  pip install -r requirements.txt
  ```
4. Al tener las dependencias instaladas, se continua con la configuración de la conexión a la base de datos. Si se hizo la importación de la base de datos de prueba es solo conectarse, para esto deberán actualizar los datos en el archivo "settings.py" de la carpeta admin.

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'PruebaTecnica',
          'USER': 'postgres',
          'PASSWORD': '####',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

En caso contrario, donde se creó la base de datos vacía. Se deben realizar las migraciones a dicha base de datos. Para hacer las migraciones se ejecuta los siguientes comandos:
  ```
    python manage.py makemigrations
    
    python manage.py migrate
  ```

Al tener las migraciones y la base de datos con las tablas que genera Django se procede a ejecutar el programa:
  ```
   python manage.py runserver
  ```

Finalmente, ya teniendo el sistema ejecutando, se tomará la URL que genera para así mismo consumir los servicios.

Documentación de los servicios [Postman Documentation](https://documenter.getpostman.com/view/18457387/2s8Z6x1YX1).

SQL [DB_Testing.zip](https://github.com/Alejandrolara21/Prueba-Tecnica-Backend-SFA/files/10304806/DB_Testing.zip)

Credenciales para administrador:
  ```
   email: testing@gmail.com
   password: 123456
  ```
