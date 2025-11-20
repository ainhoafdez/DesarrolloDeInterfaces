from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QFileDialog
)
from PySide6.QtGui import QAction, QKeySequence


class Main(QMainWindow):                            # Porque qmainwindow tiene el .menuBar()
    def __init__(self):
        super().__init__()

        # ------------------------------------------------------------------
        # ZONA DECLARATIVA
        # ------------------------------------------------------------------
        
        contenedor = QWidget()                      # Layout principal
        layout_principal = QHBoxLayout(contenedor)

        self.text_edit = QTextEdit()                # Area de escritura

        botones = QVBoxLayout()                     # Vertical Layout de los botones a la dcha

        self.btn_atras = QPushButton("↶")          # Botón deshacer
        self.btn_borrar = QPushButton("⨂")         # Botón borrar todo

        self.btn_guardar = QPushButton("Save")      # Botón guardar
        self.btn_cargar = QPushButton("Load")       # Botón cargar

        # MENU
        barra = self.menuBar()

        # Desplegables del menu Titulos
        self.h1 = QAction("H1", self)
        self.h2 = QAction("H2", self)
        self.h3 = QAction("H3", self)
        self.h4 = QAction("H4", self)
        # Desplegables del menu Insertar
        self.separador = QAction("Separador", self)
        self.link = QAction("Link", self)
        # Desplegables del menu Code
        self.linea = QAction("Line", self)
        self.bloque = QAction("Block", self)

        # ------------------------------------------------------------------
        # ZONA INICIALIZACIÓN (propiedades, layouts, menú, etc.)
        # ------------------------------------------------------------------
        self.setWindowTitle("Markdown Editor")
        self.setGeometry(100, 100, 600, 500)

        # Área de texto izquierda (QVBoxLayout)
        layout_principal.addWidget(self.text_edit)  # Agrego text edit al qhbox principal

        # Barra de botones derecha
        botones.addWidget(self.btn_atras)
        botones.addWidget(self.btn_borrar)
        botones.addWidget(self.btn_guardar)
        botones.addWidget(self.btn_cargar)
        botones.addStretch()                    # Rellena el hueco de abajo de los botones para que esten arriba

        layout_principal.addLayout(botones)     # Agrego qvbox de botones al qhbox principal

        self.setCentralWidget(contenedor)

        # --- Configuración del menu ---
        titulos_menu = barra.addMenu("&Titles ▾")
        insert_menu = barra.addMenu("&Insert ▾")
        barra.addAction(QAction("𝔹", self))
        barra.addAction(QAction("ℐ", self))
        barra.addAction(QAction("⌸", self))
        barra.addAction(QAction("1. ≡", self))
        barra.addAction(QAction("• ≡", self))
        code_menu = barra.addMenu("&Code ▾")

        titulos_menu.addAction(self.h1)
        titulos_menu.addAction(self.h2)
        titulos_menu.addAction(self.h3)
        titulos_menu.addAction(self.h4)

        insert_menu.addAction(self.separador)
        insert_menu.addAction(self.link)

        code_menu.addAction(self.linea)
        code_menu.addAction(self.bloque)

        # ------------------------------------------------------------------
        # BOTON AL CLICK
        # ------------------------------------------------------------------
        self.btn_guardar.clicked.connect(self.guardar_nota)
        self.btn_cargar.clicked.connect(self.cargar_nota)

    # ----------------------------------------------------------------------
    # FUNCIONES
    # ----------------------------------------------------------------------
    def guardar_nota(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save", "", "Text file (*.txt);;Markdown file (*.md)"
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def cargar_nota(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Load", "", "Text file (*.txt);;Markdown file (*.md)"
        )
        if file_path:
            with open(file_path, 'r') as file:
                self.text_edit.setPlainText(file.read())


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
