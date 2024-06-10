import sys
import os
from dotenv import load_dotenv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

load_dotenv()

website_url = os.getenv('WEBSITE_URL')
application_name = os.getenv('APPLICATION_NAME')

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(website_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QIcon('icon.png'))
        
        self.reload_shortcut = QShortcut(QKeySequence('F5'), self)
        self.reload_shortcut.activated.connect(self.reload_page)
        
    def reload_page(self):
        self.browser.reload()

app = QApplication(sys.argv)
QApplication.setApplicationName(application_name)
window = Browser()
app.exec_()
