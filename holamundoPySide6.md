# Mi primer "Hola mundo" en PySide6
- [Enlace al proyecto](https://github.com/ainhoafdez/DesarrolloDeInterfaces/tree/main/holamundoPySide6)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Requisitos previos](#requisitos-previos)
- [Creación y activación del entorno virtual](#creación-y-activación-del-entorno-virtual)
- [Instalación de dependencias](#instalación-de-dependencias)
- [Estructura mínima de carpetas y archivos](#estructura-mínima-de-carpetas-y-archivos)
- [Código fuente](#código-fuente)
- [Ejecución y prueba](#ejecución-y-prueba)
- [Problemas frecuentes y cómo resolverlos](#problemas-frecuentes-y-cómo-resolverlos)
- [Checklist del alumno](#checklist-del-alumno)
---

## Objetivos de aprendizaje
- Crear venv
- Instalar dependencias
- Ejecutar una ventana básica
- Entender QApplication y el ciclo de eventos.

## Requisitos previos
- Versión de Python utilizada: Python 3.13.7 (se sabe con el comando "**python --version**"
- Sistema operativo: Windows 11
- Herramientas: GitHub y Visual Studio Code

## Creación y activación del entorno virtual
- Crear venv
```bash
python -m venv venv3
venv\Scripts\activate
```
- Abrimos explorador de archivos y en la url del venv escribimos "**code .**"
- Creamos nuestros archivos main.py y ventana.py en python y ejecutamos el venv en la terminal

<img width="638" height="126" alt="Captura de pantalla 2025-10-14 122730" src="https://github.com/user-attachments/assets/c3ed85c7-13c2-47bf-91c4-41fb68eaa40a" />
<img width="1028" height="508" alt="image" src="https://github.com/user-attachments/assets/9a6b2b61-2276-4d49-923f-81ca83d2cad0" />

## Instalación de dependencias
- Instalamos PySide 6 con el comando "**pip install Pyside6**"
- Exportamos requirements.txt con el comando "**pip freeze > requirements.txt**"
- [PySide6](https://pypi.org/project/PySide6) permite a los desarrolladores de Python crear aplicaciones con interfaces gráficas (GUIs) de forma multiplataforma

<img width="1448" height="266" alt="image" src="https://github.com/user-attachments/assets/2c4880cd-3855-459c-803f-70153471d156" />


## Estructura mínima de carpetas y archivos
Separamos la clase Main de la clase Ventana para que Ventana tenga el constructor y la ventana emergente con el texto y el Main la ejecute.
Así logramos un código limpio y ordenado entre clases, sin mezclar la función de cada una.

<img width="202" height="377" alt="image" src="https://github.com/user-attachments/assets/cf92370b-8777-4d66-b9ea-3dffcc8a9bd4" />

## Código fuente

```python

#Importamos las clases QApplication, QLabel y QWidget # del módulo
#QtWidgets del paquete
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from Ventana import Ventana

if __name__ == "__main__":
        #Cada app es una instancia de QAPP
    app = QApplication([])
        
        #Crear objeto ventana
    ventana1 = Ventana()

        #Mostrar ventana por defecto con componentes ocultos
    ventana1.show()

        #Iniciar el bucle de eventos
    app.exec()
    
```

```python
from PySide6.QtWidgets import QApplication, QLabel, QWidget

'''
Clase Ventana, hereda de QWidget, componente base.
'''
 
class Ventana(QWidget):    
    def _init_(self):
        # LLama al constructor de la superclase
        super()._init_()

        # Asigna el nombre de la ventana
        self.setWindowTitle("Ventana")
        
        # Asigna el tamaño de la ventana
        self.setGeometry(100,100,300,200)
        
        # Etiqueta con ventana como elemento principal
        self.etiqueta1 = QLabel("Hola Mundo! ", self)
```

## Ejecución y prueba

- Comando para ejecutar la app desde /src: "**python src/main.py**"
- ¿Cómo cambio el título o tamaño de la ventana emergente? :
```python

# Asigna el nombre de la ventana
        self.setWindowTitle("Ventana")
        
# Asigna el tamaño de la ventana
        self.setGeometry(100,100,300,200)

# Etiqueta con ventana como elemento principal
        self.etiqueta1 = QLabel("Hola Mundo! ", self) #Contenido de la ventana
```

## Problemas frecuentes y cómo resolverlos
- El intérprete no es el del venv
- ModuleNotFoundError: PySide6
- Conflictos de ruta al ejecutar python desde otra carpeta

## Checklist del alumno
- [X] He creado y activado el venv.
- [X] He instalado PySide6 y generado requirements.txt.
- [X] He separado main.py y ventana.py.
- [X] He incluido bloques de código con comentarios.
- [X] He explicado QApplication, widgets y app.exec().
- [X] He probado la app y documentado la ejecución.
