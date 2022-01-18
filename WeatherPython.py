from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import (QApplication,QMessageBox,QMainWindow,QMenuBar,QGridLayout, QLineEdit, QListWidget, QTextEdit, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QFormLayout)
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('71579b940908f2fe19ab16742ab07157')
mgr = owm.weather_manager()

app = QApplication([])
main_l = QWidget()
row1 = QVBoxLayout()
rows = QHBoxLayout()
main_l.setWindowTitle('Погода')
main_l.resize(600, 300)
palette = QPalette()
palette.setBrush(QPalette.Background, QBrush(QPixmap(".\Your photo")))
main_l.setPalette(palette)

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QVBoxLayout()
row4 = QVBoxLayout()

town = QLineEdit()
appdate = QPushButton('Поиск')
delete = QPushButton('Удалить текст')
temputer = QLabel('<b>Температура:</b>')
info_temp = QLabel('-')
wind = QLabel('<b>Скорость ветра:</b>')
info_wind = QLabel('-')
clouds = QLabel('<b>Процент облаков:</b>')
info_cloud = QLabel('-')


row1.addWidget(town)
row1.addWidget(appdate)
row1.addWidget(delete)
row2.addWidget(temputer, alignment = Qt.AlignTop | Qt.AlignCenter)
row2.addWidget(info_temp, alignment = Qt.AlignTop)
row2.addWidget(wind, alignment = Qt.AlignTop | Qt.AlignCenter)
row2.addWidget(info_wind, alignment = Qt.AlignTop)
row2.addWidget(clouds, alignment = Qt.AlignTop | Qt.AlignCenter)
row2.addWidget(info_cloud, alignment = Qt.AlignTop)

def weather():
    try:
        observation = mgr.weather_at_place(town.text())
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        if int(temp) <= -25:
            info_temp.setText(str(round(temp)) + ' 🥶')
        if int(temp) >= 25:
            info_temp.setText(str(round(temp)) + ' 🥵')
        if int(temp) < 25 and int(temp) > -25:
            info_temp.setText(str(round(temp)) + '🙂')
            
        veter = w.wind()["speed"]
        if int(veter) >= 0 and int(veter) <= 3.99999999999:
            info_wind.setText(str(veter) +'м/с ࿓')
        if int(veter) >= 4 and int(veter) <= 6:
            info_wind.setText(str(veter) +'м/с ༄')
        if int(veter) >= 6.0000000000001:
            info_wind.setText(str(veter) +'м/с 💨') 
        oblaca = w.clouds
        if int(round(oblaca)) <= 50:
            info_cloud.setText(str(round(oblaca)) + '🌤')
        if int(round(oblaca)) <= 80 and int(round(oblaca)) >= 51:
            info_cloud.setText(str(round(oblaca)) + '⛅')
        if int(round(oblaca)) >= 81:
            info_cloud.setText(str(round(oblaca)) + '🌥')
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Проверьте название города")
        msg.exec_()

def deletee():
    town.setText('')  

row3.addLayout(row1)  
row3.addLayout(row2)

main_l.setLayout(row3)
appdate.clicked.connect(weather)
delete.clicked.connect(deletee)
main_l.show()
app.exec_()
#https://tproger.ru/translations/pyqt-apps/
