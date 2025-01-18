# Automatización - Prueba Inlaze
Requerimiento 1

# Como clonar el repositorio
Paso 1: Instalar git 

        Windows: https://git-scm.com/download/win 
        MAC: https://git-scm.com/download/mac 
        General: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git

Paso 2: Abrir git por terminal Windows: CMD MAC: Terminal

Paso 3: Ingresar a la carpeta donde se va a clonar el proyecto.

- ls
- cd Documents/

Paso 4: Para clonar el proyecto se debe ejecutar el siguiente comando git clone
- https://github.com/luisDevPKG/PruebaInlaze.git

# Como configurar el entorno para la ejecución de la automatizacion
Paso 1: Descargar e instalar python en la versión estable: https://www.python.org/downloads/
Paso 2: Descargar e instalar selenium en la versión estable: https://www.selenium.dev/downloads/
Paso 3: Descargar e instalar pycharm en la versión community:
    -Windows: https://www.jetbrains.com/es-es/pycharm/download/#section=windows
    -MAC: https://www.jetbrains.com/es-es/pycharm/download/#section=mac
    
Paso 5: Configuracion del WebDriver en el script
-Abrir Pycharm como administrador, abrir el proyecto de automatizacion

Paso 6: Abrir el Terminal

Paso 7: Instalar las librerias de Selenium, Pytest y Webdriver Manager
-pip install selenium o py -m pip install selenium
-pip install pytest o py -m pip install pytest
-pip install webdriver-manager o py -m pip install webdriver-manager
En caso de que para SO Windows No se visualicen cambios, abrir cmd, ejecutarlo como administrador y ejecutar los mismos codigos mencionados anteiormente

Paso 8: Hacer clic y ejecutar los tests desde su respectivo archivo test_registration_page y test_login_page