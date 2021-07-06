# OverTicket Ecommerce
Web construida con Django RestFramework + Vue

# SetUp
Para correr la aplicacion sin errores debes:

### Crear un ambiente virtual
Para instalarlo: <br>
    - pip install virtualenv

Para crearlo: <br>
    - virtualenv <nombre>

Para activarlo: <br>
    - ./nombre/Scripts/activate

### Instalar Django + librerias (Dentro del ambiente virtual)
pip install django <br>
pip install django-rest-framework <br>
pip install django-cors-headers <br>
pip install djoser <br>
pip install pillow <br>
pip install stripe <br>

### Correr el servidor de Django
En la terminal escribir <br>
py manage.py runserver

Para agregar mas eventos ingrese al panel de administracion con las siguientes credenciales <br>
Usuario: admin <br>
Pass: admin <br>

### Correr el FrontEnd
Dentro de la carpeta Front deberas instalar el package.json (npm install <package_name>) <br>
Una vez hecho eso ingresa el comando <br>
npm run serve