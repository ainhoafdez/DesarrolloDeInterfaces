# Importamos las clases QApplication, QLabel y QWidget # del módulo
# QtWidgets del paquete
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from Ventana01 import Ventana01

if __name__ == "__main__":
        #Cada app es una instancia de QAPP
    app = QApplication([])
        
        #Crear objeto ventana
    ventana1 = Ventana01()

        #Mostrar ventana por defecto con componentes ocultos
    ventana1.show()

        #Iniciar el bucle de eventos
    app.exec()