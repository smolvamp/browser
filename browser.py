
from PyQt6.QtCore import * #type: ignore
from PyQt6.QtWidgets import *#type: ignore
from PyQt6.QtWebEngineWidgets import *#type: ignore
from PyQt6.QtWebEngineCore import *#type: ignore
from PyQt6.QtGui import *#type: ignore
import sys
import os
class broswer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.home= QWebEngineView()
        
    def show(self):
        self.showMaximized()
        path_icon= os.path.join("browser/src/","icon.jpeg")
        try:
            icon=QIcon(path_icon)
            self.setWindowIcon(icon)
        except Exception as e:
            print(e)
        self.home.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.home)
        self.nav()
        self.home.page().profile().downloadRequested.connect(self.download) #type: ignore
    def nav(self):
        navbar= QToolBar()
        self.addToolBar(navbar)
        #back
        path_back= os.path.join("browser/src/","previous.png")
        back= QAction(QIcon(path_back),'back',self)
        back.triggered.connect(self.home.back)
        navbar.addAction(back)
        #forward
        path_forward= os.path.join("browser/src/","next-button.png")
        forward= QAction(QIcon(path_forward),'forward',self)
        forward.triggered.connect(self.home.forward)
        navbar.addAction(forward)
        #reload
        path_reload= os.path.join("browser/src","power.png")
        reload= QAction(QIcon(path_reload),"reload",self)
        reload.triggered.connect(self.home.reload)
        navbar.addAction(reload)     
        #search_bar   
        self.bar= QLineEdit()
        self.bar.setStyleSheet("QLineEdit"
                               "{"
                               "background-color:#262626;"
                               "border: 2px solid #262626;"
                               "border-radius:5px 5px 5px 5px ;"
                               "}")
        self.bar.returnPressed.connect(self.url)
        navbar.addWidget(self.bar)
        self.home.urlChanged.connect(self.search)  
        
    def url(self):
        link= self.bar.text()
        self.home.setUrl(QUrl(link))
    def search(self,u):
        self.bar.setText(u.toString())
    def download(self, requested_file):
        file= QFileDialog(self)
        file.setFileMode(QFileDialog.FileMode.Directory)        
        file.setOption(QFileDialog.Option.ShowDirsOnly)
        if file.exec():
           # requested_file.setPath(os.path.join(file.selectedFiles()[0], requested_file.suggestedFileName()))
            requested_file.accept()
        else:
            requested_file.cancel()
        
app= QApplication(sys.argv)
browser= broswer()
browser.show()
sys.exit(app.exec())
