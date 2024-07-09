#запрограммируй сложный тест
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
#создание приложения и главного окна
app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс от Crazy People')
win.resize(400, 200)
que = QLabel('Как звали первого ютуб-блогера, набравшего 100000000 подписчиков?')
#создание виджетов главного окна
ans1 = QRadioButton('Рэт и Линк')
ans2 = QRadioButton('TheBrianMaps')
ans3 = QRadioButton('SlivkiShow')
ans4 = QRadioButton('PewDiePie')
ans5 = QRadioButton('Mister Max')
ans6 = QRadioButton('EeOneGuy')
#расположение виджетов по лэйаутам
h_line1 = QHBoxLayout()
h_line1.addWidget(que)

h_line2 = QHBoxLayout()
h_line2.addWidget(ans1)
h_line2.addWidget(ans2)

h_line3 = QHBoxLayout()
h_line3.addWidget(ans3)
h_line3.addWidget(ans4)

h_line4 = QHBoxLayout()
h_line4.addWidget(ans5)
h_line4.addWidget(ans6)

v_line = QVBoxLayout()
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)
v_line.addLayout(h_line4)

win.setLayout(v_line)
#обработка нажатий на переключатели
def show_win():
    win_win = QMessageBox()
    win_win.setText('Вы выиграли встречу с создателями канала!')
    win_win.exec_()

def show_lose():
    win_lose = QMessageBox()
    win_lose.setText('Повезёт в другой раз!')
    win_lose.exec_()

ans1.clicked.connect(show_lose)
ans2.clicked.connect(show_lose)
ans3.clicked.connect(show_lose)
ans4.clicked.connect(show_win)
ans5.clicked.connect(show_lose)
ans6.clicked.connect(show_lose)
#отображение окна приложения 
win.show()
app.exec_()