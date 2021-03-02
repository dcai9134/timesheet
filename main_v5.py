import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QMessageBox,
                             QDesktopWidget, QGridLayout, QLabel, QVBoxLayout,
                             QTabWidget, QMainWindow, QComboBox, QScrollArea)
from label import lb_db


class Main_Window(QMainWindow):
    """Draw main window GUI"""
    def __init__(self):
        super().__init__()

        self.initUI()

        self.central_widget = tab(self)
        self.setCentralWidget(self.central_widget)

    def initUI(self):
        """Main window size and structure"""
        self.setGeometry(1000, 1000, 1000, 500)
        self.setWindowTitle('Timesheet Application')
        self.center()

    def center(self):
        """Function to center a window"""
        window_geom = self.frameGeometry()
        desk_center = QDesktopWidget().availableGeometry().center()
        window_geom.moveCenter(desk_center)
        self.move(window_geom.topLeft())


class tab(QWidget):
    """Create tab structure"""
    def __init__(self, parent):
        super().__init__(parent)
        self.tab = QTabWidget()
        self.layout = QGridLayout(self)

        self.addtabs()

        self.layout.addWidget(self.tab)

    def addtabs(self):
        self.tab.addTab(jobcode(self), lb_db['tab_title']['jc'])
        self.tab.addTab(monday(self), lb_db['tab_title']['mon'])
        self.tab.addTab(weekly(self), lb_db['tab_title']['week'])
        self.tab.addTab(graph(self), lb_db['tab_title']['graph'])


class jobcode(QWidget):
    """Job Code Tab"""
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)


class monday(QWidget):
    """Monday Tab"""
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.persist_UI()

    def persist_UI(self):
        self.persist = persist(self, day=lb_db['tab_title']['mon'])
        self.layout.addWidget(self.persist)


class weekly(QWidget):
    """Weekly Summary Tab"""
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)


class graph(QWidget):
    """Graphical Summary Tab"""
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)


class persist(QWidget):
    def __init__(self, parent, day):
        super().__init__(parent)
        self.initUI()
        self.titles(day)
        self.activejob()

    def initUI(self):
        self.layout = QGridLayout(self)

        self.scroll = QScrollArea()
        self.layout.addWidget(self.scroll)

    def titles(self, day):
        self.title = QLabel(lb_db['persist']['title'])
        self.description = QLabel(lb_db['persist']['description'])
        self.active_job = QLabel(lb_db['persist']['active'])
        self.time_col_title = QLabel(day)
        self.time_spent = QLabel(lb_db['persist']['timespent'])
        self.layout.addWidget(self.title, 1, 0)
        self.layout.addWidget(self.description, 2, 0)
        self.layout.addWidget(self.active_job, 2, 1)
        self.layout.addWidget(self.time_col_title, 3, 1)
        self.layout.addWidget(self.time_spent, 3, 2)

    def activejob(self):
        self.active_job_box = QComboBox()
        self.layout.addWidget(self.active_job_box, 2, 2)



app = QApplication([])
GUI = Main_Window()
GUI.show()
sys.exit(app.exec_())
