from PySide6.QtWidgets import QApplication, QLabel, QWidget

'''
Clase Ventana 01, hereda de QWidget, componente base.
'''
 
class Ventana01(QWidget):

    def __init__(self):

        super().__init__()

        self.mensajeCambiado = False # Controla si el mensaje a cambiado

        self.setWindowTitle("Ventana con evento")
        self.setGeometry(100,100,400,300)

        self.label = QLabel("Haz click en cualquier parte de la ventana", self)
        self.label.move(50,150)

        # self.label.actionEvent = self.cambiarMensaje

    # def cambiarMensaje(self, event):

    #     if not self.mensajeCambiado:
    #         self.label.setText("Has hecho click en la ventana")
    #         self.mensajeCambiado = True
    
    def mousePressEvent(self, event): # Detecta el click
        
        if not self.mensajeCambiado:
            self.label.setText("Has hecho click en la ventana")
            self.mensajeCambiado = True
        else:
            self.label.setText("Has vuelto a hacer click en la ventana")
            self.mensajeCambiado = False

    def mousePressEvent(self, event): # Detecta el click
        
        if not self.mensajeCambiado:
            self.label.setText("Has hecho click en el label")
            self.mensajeCambiado = True
        else:
            self.label.setText("Has vuelto a hacer click en el label")
            self.mensajeCambiado = False