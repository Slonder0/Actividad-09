from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from administradora import Administradora
from particula import Particula
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen,QColor,QTransform

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.administrador = Administradora()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_final.clicked.connect(self.agregar_final)
        self.ui.Agregar_Inicio.clicked.connect(self.agregar_inicio)
        self.ui.Mostrar.clicked.connect(self.ver)
        
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        
        self.ui.view_button.clicked.connect(self.mostrar_tabla)
        self.ui.search_button.clicked.connect(self.buscar_tabla)
        
        self.ui.Dibujar.clicked.connect(self.dibujar)
        self.ui.Limpiar.clicked.connect(self.limpiar)
        
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
    def wheelEvent(self,event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
        
    
    
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.administrador:
            origenx = int(particula.origen_x)
            origeny = int(particula.origen_y)
            destinox = int(particula.destino_x)
            destinoy = int(particula.destino_y)
            
            red = int(particula.red)
            green = int(particula.green)
            blue= int(particula.blue)
            
            color = QColor(red,green,blue)
            pen.setColor(color)
            
            self.scene.addEllipse(origenx,origeny,3,3,pen)
            self.scene.addEllipse(destinox,destinoy,3,3,pen)
            self.scene.addLine(origenx,origeny,destinox,destinoy,pen)
            
        
        
    @Slot()
    def limpiar(self):
        self.scene.clear()   
     
    @Slot()
    def buscar_tabla(self):
        id = self.ui.search_line.text()
        encontrado = False
        
        for particula in self.administrador:
            
            if int(id)  ==  particula.id:
                self.ui.table.clear()
                self.ui.table.setRowCount(1)
                headers = ["ID","Origen X","Origen Y","Destino X","Destino Y","Red","Green","Blue","Distancia"]
                self.ui.table.setHorizontalHeaderLabels(headers)
                
                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origen_x))
                origeny_widget = QTableWidgetItem(str(particula.origen_y))
                destinox_widget = QTableWidgetItem(str(particula.destino_x))
                destinoy_widget = QTableWidgetItem(str(particula.destino_y))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
            
                self.ui.table.setItem(0,0,id_widget)
                self.ui.table.setItem(0,1,origenx_widget)
                self.ui.table.setItem(0,2,origeny_widget)
                self.ui.table.setItem(0,3,destinox_widget)
                self.ui.table.setItem(0,4,destinoy_widget)
                self.ui.table.setItem(0,5,red_widget)
                self.ui.table.setItem(0,6,green_widget)
                self.ui.table.setItem(0,7,blue_widget)
                self.ui.table.setItem(0,8,distancia_widget)
                
                encontrado = True
                
                return    
            
        if not encontrado:
            QMessageBox.warning(self,'Atencíon',f'La particula con ID "{id}" no fue encontrado')
                
        
     
     
     
     
    @Slot()
    def mostrar_tabla(self):
        self.ui.table.setColumnCount(9)
        headers = ["ID","Origen X","Origen Y","Destino X","Destino Y","Red","Green","Blue","Distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        
        self.ui.table.setRowCount(len(self.administrador))

        row = 0
        for particula in self.administrador:
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origen_x))
            origeny_widget = QTableWidgetItem(str(particula.origen_y))
            destinox_widget = QTableWidgetItem(str(particula.destino_x))
            destinoy_widget = QTableWidgetItem(str(particula.destino_y))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            
            self.ui.table.setItem(row,0,id_widget)
            self.ui.table.setItem(row,1,origenx_widget)
            self.ui.table.setItem(row,2,origeny_widget)
            self.ui.table.setItem(row,3,destinox_widget)
            self.ui.table.setItem(row,4,destinoy_widget)
            self.ui.table.setItem(row,5,red_widget)
            self.ui.table.setItem(row,6,green_widget)
            self.ui.table.setItem(row,7,blue_widget)
            self.ui.table.setItem(row,8,distancia_widget)
            
            row += 1
            
        
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self,'Abrir Archivo','.','JSON (*.json)')[0]
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(self,"Exito","Se abrió el archivo de" + ubicacion)
        else:
            QMessageBox.information(self,"Error","No se pudo abrir el archivo de " + ubicacion)
        
        
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self,'Guardar Archivo','.','JSON (*.json)')[0]
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(self,"Exito","Se creó el archivo con exito en " + ubicacion)
        else:
            QMessageBox.information(self,"Error","No se pudo crear el archivo en " + ubicacion)
            
        
    
    @Slot()   
    def ver(self):
        self.ui.Print.clear()
        self.ui.Print.insertPlainText(str(self.administrador))    
        
        
        
    @Slot()   
    def agregar_final(self):
        ID = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        
        
        particula1 = Particula(ID,OrigenX,OrigenY,DestinoX,DestinoY,Red,Green,Blue)
        self.administrador.agregar_final(particula1)
    
    @Slot()    
    def agregar_inicio(self):
        ID = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()
        
        particula1 = Particula(ID,OrigenX,OrigenY,DestinoX,DestinoY,Red,Green,Blue)
        self.administrador.agregar_inicio(particula1)
        
  