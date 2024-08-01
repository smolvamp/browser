import re
from webbrowser import *
from PyQt6.QtCore import * 
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *
from PyQt6.QtGui import *
import sys


class broswer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.home= QWebEngineView()
        
    def show(self):
        self.showMaximized()
        try:
            icon=QIcon('~/Music/icon.ico')
            self.setWindowIcon(icon)
        except Exception as e:
            print(e)
        self.home.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.home)
        self.nav()
        self.home.page().profile().downloadRequested.connect(self.download)
    def nav(self):
        navbar= QToolBar()
        self.addToolBar(navbar)
        #back
        back= QAction(QIcon('previous.png'),'back',self)
        back.triggered.connect(self.home.back)
        navbar.addAction(back)
        #forward
        forward= QAction(QIcon('next-button.png'),'forward',self)
        forward.triggered.connect(self.home.forward)
        navbar.addAction(forward)
        #reload
        reload= QAction(QIcon('power.png'),"reload",self)
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