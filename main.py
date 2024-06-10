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

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(website_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        icon_path = resource_path('icon.png')
        self.setWindowIcon(QIcon(icon_path))
        
        self.reload_shortcut = QShortcut(QKeySequence('F5'), self)
        self.reload_shortcut.activated.connect(self.reload_page)
        
    def reload_page(self):
        self.browser.reload()

app = QApplication(sys.argv)
QApplication.setApplicationName(application_name)
window = Browser()
app.exec_()
