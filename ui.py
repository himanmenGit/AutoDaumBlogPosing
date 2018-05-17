import sys
from PyQt5.QtWidgets import *

from posting import DaumPosting


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.id = None
        self.password = None
        self.title = None
        self.repeat = None
        self.content = None
        self.log = None

    def setupUI(self):
        UI_WIDTH = 1024
        UI_HEIGHT = 768

        centerPoint = QDesktopWidget().screenGeometry().center()
        self.setGeometry(centerPoint.x() - UI_WIDTH / 2, centerPoint.y() - UI_HEIGHT / 2, UI_WIDTH, UI_HEIGHT)

        label1 = QLabel("아이디")
        label2 = QLabel("비밀번호")
        repeat = QLabel('포스팅 수')
        title = QLabel('제목')
        label3 = QLabel("내용")
        label4 = QLabel("로그")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setEchoMode(QLineEdit.Password)

        self.titleEdit = QLineEdit()
        self.repeatEdit = QLineEdit()

        self.linetext = QTextEdit()

        self.linelog1 = QTextEdit()
        self.linelog1.setReadOnly(True)

        self.postingBtn = QPushButton("Posting")
        self.postingBtn.clicked.connect(self.Posting)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)

        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        layout.addWidget(title, 2, 0)
        layout.addWidget(self.titleEdit, 2, 1)

        layout.addWidget(repeat, 3, 0)
        layout.addWidget(self.repeatEdit, 3, 1)

        layout.addWidget(label3, 4, 0)
        layout.addWidget(self.linetext, 4, 1)

        layout.addWidget(label4, 5, 0)
        layout.addWidget(self.linelog1, 5, 1)

        layout.addWidget(self.postingBtn, 6, 1)

        self.setLayout(layout)

    def Posting(self):
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.title = self.titleEdit.text()
        self.repeat = self.repeatEdit.text()
        self.content = self.linetext.toPlainText()
        self.log = self.linelog1.toPlainText()

        dp = DaumPosting(ui=self, id=self.id, pw=self.password, title=self.title, repeat=self.repeat,
                         content=self.content)
        dp.setBrowser()

    def logUpdate(self, log):
        self.linelog1.append(log)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
