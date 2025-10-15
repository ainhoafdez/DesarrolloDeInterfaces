from PySide6.QtWidgets import QApplication, QLabel, QWidget

'''
Clase Ventana, hereda de QWidget, componente base.
'''
 
class Ventana(QWidget):

    def __init__(self):
        # LLama al constructor de la superclase
        super().__init__()

        # Asigna el nombre de la ventana
        self.setWindowTitle("Ventana")
        
        # Asigna el tamaño de la ventana
        self.setGeometry(100,100,400,300)
        
        # Etiqueta con ventana como elemento principal
        self.etiqueta1 = QLabel("Hola Mundo", self)