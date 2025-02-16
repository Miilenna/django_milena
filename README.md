# django_milena

## ACTIVITAT 13

### Actividad 1:
Página de teachers y estudiantes desde la aplicación:
![alumn.png](ACTIVITAT_13/recursos/alumn.png)
![profes.png](ACTIVITAT_13/recursos/profes.png)

Página de teachers y estudiantes desde el proyecto:
![header_alumn.png](ACTIVITAT_13/recursos/header_alumn.png)
![header_profe.png](ACTIVITAT_13/recursos/header_profe.png)

### Actividad 2:
Video:
https://youtu.be/fsFmCkgOEWs

## ACTIVITAT 14

### Configuración del proyecto:

![conn.png](ACTIVITAT_13/recursos/act14/conn.png)
![bbdd.png](ACTIVITAT_13/recursos/act14/bbdd.png)
![templates.png](ACTIVITAT_13/recursos/act14/templates.png)
![templates_config.png](ACTIVITAT_13/recursos/act14/templates_config.png)
![path.png](ACTIVITAT_13/recursos/act14/path.png)

### Creación de la aplicación:
El comando para crear la app:
![comando_crear_app.png](ACTIVITAT_13/recursos/act14/comando_crear_app.png)
![urls_trucada_metodes.png](ACTIVITAT_13/recursos/act14/urls_trucada_metodes.png)
![metodos_correctos.png](ACTIVITAT_13/recursos/act14/metodos_correctos.png)

### Modelo usuario:
![makemigration.png](ACTIVITAT_13/recursos/act14/makemigration.png)
![migrate.png](ACTIVITAT_13/recursos/act14/migrate.png)
![tabla_login.png](ACTIVITAT_13/recursos/act14/tabla_login.png)

## Documentación de la funcionalidad del login sin session
Hacer un login sin session permite al usuario acceder sin tener que autentificarse ni iniciar sesión, de esta manera no es necesario hacer una consulta a la base de datos. 
### **Funcionamiento**
1. Cuando un usuario le da al botón de acceder sin iniciar sesión lo que hace es dirigirle directamente a la página de inicio.
2. En la página de inicio se le asigna el rol de invitado ya que no ha entrado con ninguna sesión.

![2025-02-16 22-22-48.gif](ACTIVITAT_13/recursos/act14/2025-02-16%2022-22-48.gif)


## Documentación de la funcionalidad del login con session
Al hacer un login con session permite al usuario autentificarse con su correo electrónico y contraseña, que esta registrado en la base de datos.
### **Funcionamiento**
1. El usuario introduce su email y contraseña en el formulario.
2. Si las credenciales son correctas, se guarda su id y nombre en la sesión.
3. Después se redirige a la página de inicio, donde se muestra el nombre del usuario autentificado.

![2025-02-16 22-22-02.gif](ACTIVITAT_13/recursos/act14/2025-02-16%2022-22-02.gif)


## Documentación de la funcionalidad del logout
Permite a los usuarios cerrar sesión, borrando la información de la sesión y devolviendo al usuario a la página del login.
### **Funcionamiento**
1. Borra toda la información de la sesión manual.
2. También cierra la sesión con Django.
3. Redirige al usuario a la pantalla del login.



