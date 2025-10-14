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