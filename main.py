# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from moviepy.editor import *
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
import threading
import sys
from pytube import YouTube
from tkinter import messagebox

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
centralwidget = QtWidgets.QWidget(MainWindow)
centralwidget.setObjectName("centralwidget")
MainWindow.setCentralWidget(centralwidget)
MainWindow.resize(701, 364)
MainWindow.setMaximumSize(701, 364)

def searchdir_func():
    global file_path

    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly

    file_dialog = QFileDialog()
    file_dialog.setOptions(options)
    file_path, _ = file_dialog.getOpenFileName(None, 'Abrir archivo', '', 'Archivos mp4 (*.mp4);;Archivos 3gpp (*.3gpp)')

    if file_path:
        file_entry.setText(file_path)

def convertir_func():
    nombre = os.path.splitext(os.path.basename(file_path))[0]
    messagebox.showinfo("MP4 To MP3", f"Convirtiendo archivo {nombre} a .mp3")
    
    tl = VideoFileClip(file_path)
    audio = tl.audio
    audio.write_audiofile(f'output/{nombre}.mp3')

    messagebox.showinfo("MP4 To MP3", f"Archivo movido a la carpeta: output/{nombre}.mp3")

    tl.close()
    audio.close()

def mp3_func():
    global file_entry

    ventana = QDialog(MainWindow)
    ventana.setObjectName("ventana")
    ventana.resize(286, 241)
    ventana.setMaximumSize(286, 241)
    ventana.setWhatsThis("")
    ventana.setWindowTitle("MP4 To MP3")

    menu = QtWidgets.QFrame(ventana)
    menu.setGeometry(QtCore.QRect(-120, 0, 411, 80))
    menu.setStyleSheet("background-color: rgb(206, 206, 206);")
    menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
    menu.setFrameShadow(QtWidgets.QFrame.Raised)
    menu.setObjectName("menu")

    titulo = QtWidgets.QLabel(menu)
    titulo.setGeometry(QtCore.QRect(180, 10, 201, 51))
    titulo.setStyleSheet("font: 22pt \"Arial\";")
    titulo.setObjectName("titulo")
    titulo.setText("MP4 To MP3")

    file_entry = QtWidgets.QLineEdit(ventana)
    file_entry.setGeometry(QtCore.QRect(70, 130, 111, 21))
    file_entry.setStyleSheet("border-radius: 6px;\n""color: #000000;\n""background-color: rgb(198, 198, 198);")
    file_entry.setText("")
    file_entry.setObjectName("file_entry")

    mp4_label = QtWidgets.QLabel(ventana)
    mp4_label.setGeometry(QtCore.QRect(90, 110, 91, 16))
    mp4_label.setStyleSheet("font: 7pt \"Verdana\";")
    mp4_label.setObjectName("mp4_label")

    searchdir_btn = QtWidgets.QPushButton(ventana)
    searchdir_btn.setGeometry(QtCore.QRect(190, 130, 31, 21))
    searchdir_btn.setObjectName("searchdir_btn")
    searchdir_btn.clicked.connect(searchdir_func)

    convertir_btn = QtWidgets.QPushButton(ventana)
    convertir_btn.setGeometry(QtCore.QRect(80, 170, 91, 31))
    convertir_btn.setObjectName("convertir_btn")
    convertir_btn.clicked.connect(convertir_func)

    searchdir_btn.setText("►")
    convertir_btn.setText("Convertir")
    mp4_label.setText("Archivo MP4:")
    
    ventana.exec_()

##-------------------------
def descarga(calidad, video):
    if calidad == "Mayor calidad Disponible":
        try:
           maximo = video.streams.get_highest_resolution()
           maximo.download(output_path='output/')
           progressBar.setValue(100)

           messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")
    elif calidad == "1080p":
        try:
           down = video.streams.filter(progressive=True, file_extension='mp4', res=calidad).first()
           down.download(output_path='output/')
           progressBar.setValue(100)
           
           messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")
    elif calidad == "720p":
        try:
           down = video.streams.filter(progressive=True, file_extension='mp4', res=calidad).first()
           down.download(output_path='output/')
           progressBar.setValue(100)

           messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")
    elif calidad == "480p":
        try:
           down = video.streams.filter(progressive=True, file_extension='mp4', res=calidad).first()
           down.download(output_path='output/')
           progressBar.setValue(100)

           messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")
    elif calidad == "360p":
        try:
           down = video.streams.filter(progressive=True, file_extension='mp4', res=calidad).first()
           down.download(output_path='output/')
           progressBar.setValue(100)

           messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
        except Exception as e:
            messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")
    elif calidad == "144p":
       try:
          down = video.streams.filter(progressive=True, res=calidad).first()
          down.download(output_path='output/')
          progressBar.setValue(100)

          messagebox.showinfo("Youtube Downloader", "Video descargado exitosamente.")
       except Exception as e:
           messagebox.showerror("Youtube Downloader", f"A ocurrido un error al intentar descargar el video: {e}")

def descargar_func():
    url = entry_video_url.text()
    calidad = comboBox.currentText()
    video = YouTube(url)

    mensaje = QMessageBox()
    mensaje.setIcon(QMessageBox.Information)
    mensaje.setText(f"Descargando video: {video.title}")
    mensaje.setWindowTitle("Youtube Downloader")
    mensaje.exec_()

    th = threading.Thread(target=descarga, args=(calidad, video))
    th.start()


#------------------------------------------#
frame = QtWidgets.QFrame(centralwidget)
frame.setGeometry(QtCore.QRect(0, 0, 711, 121))
frame.setStyleSheet("background-color: rgb(255, 255, 255);")
frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
frame.setFrameShadow(QtWidgets.QFrame.Raised)
frame.setObjectName("frame")

titulo_label = QtWidgets.QLabel(frame)
titulo_label.setGeometry(QtCore.QRect(200, 20, 381, 61))
font = QtGui.QFont()
font.setFamily("Arial")
font.setPointSize(26)
font.setBold(False)
font.setItalic(False)
font.setWeight(50)

titulo_label.setFont(font)
titulo_label.setStyleSheet("font: 26pt \"Arial\";")
titulo_label.setObjectName("titulo_label")
image = QtWidgets.QLabel(frame)
image.setGeometry(QtCore.QRect(20, 10, 131, 101))
image.setText("")
image.setPixmap(QtGui.QPixmap("icons/Youtube_logo.png"))
image.setObjectName("image")

mp3_conver_btn = QtWidgets.QPushButton(frame)
mp3_conver_btn.setGeometry(QtCore.QRect(600, 30, 81, 61))
mp3_conver_btn.setStyleSheet("border-radius: 10px;\n""background-color: rgb(199, 199, 199);\n""")
mp3_conver_btn.setText("")
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("icons/mp3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
mp3_conver_btn.setIcon(icon)
mp3_conver_btn.setIconSize(QtCore.QSize(45, 45))
mp3_conver_btn.setObjectName("mp3_conver_btn")
mp3_conver_btn.clicked.connect(mp3_func)

separador = QtWidgets.QFrame(centralwidget)
separador.setGeometry(QtCore.QRect(0, 125, 701, 41))
separador.setFrameShape(QtWidgets.QFrame.HLine)
separador.setFrameShadow(QtWidgets.QFrame.Sunken)
separador.setObjectName("separador")

label_video_url = QtWidgets.QLabel(centralwidget)
label_video_url.setGeometry(QtCore.QRect(30, 180, 91, 16))
label_video_url.setStyleSheet("font: 11pt \"Verdana\";")
label_video_url.setObjectName("label_video_url")

entry_video_url = QtWidgets.QLineEdit(centralwidget)
entry_video_url.setGeometry(QtCore.QRect(120, 180, 541, 21))
entry_video_url.setText("")
entry_video_url.setFrame(False)
entry_video_url.setAlignment(QtCore.Qt.AlignCenter)
entry_video_url.setObjectName("entry_video_url")

calidad_label = QtWidgets.QLabel(centralwidget)
calidad_label.setGeometry(QtCore.QRect(30, 230, 91, 16))
calidad_label.setStyleSheet("font: 11pt \"Verdana\";")
calidad_label.setObjectName("calidad_label")

comboBox = QtWidgets.QComboBox(centralwidget)
comboBox.setGeometry(QtCore.QRect(100, 230, 141, 22))
comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
comboBox.setFrame(True)
comboBox.setObjectName("comboBox")
comboBox.addItem("")
comboBox.addItem("")
comboBox.addItem("")
comboBox.addItem("")
comboBox.addItem("")
comboBox.addItem("")
comboBox.setItemText(4, "360p")
comboBox.setItemText(5, "144p")

frame_bar = QtWidgets.QFrame(centralwidget)
frame_bar.setGeometry(QtCore.QRect(0, 300, 701, 41))
frame_bar.setStyleSheet("background-color: rgb(197, 197, 197);")
frame_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
frame_bar.setFrameShadow(QtWidgets.QFrame.Raised)
frame_bar.setObjectName("frame_bar")

progressBar = QtWidgets.QProgressBar(frame_bar)
progressBar.setGeometry(QtCore.QRect(10, 10, 581, 21))
progressBar.setProperty("value", 24)
progressBar.setAlignment(QtCore.Qt.AlignCenter)
progressBar.setObjectName("progressBar")

pushButton = QtWidgets.QPushButton(frame_bar)
pushButton.setGeometry(QtCore.QRect(610, 10, 81, 21))
font = QtGui.QFont()
font.setFamily("Calibri Light")
font.setPointSize(12)
font.setBold(False)
font.setItalic(False)
font.setWeight(3)

pushButton.setFont(font)
pushButton.setStyleSheet("font: 25 12pt \"Calibri Light\";\n""color: rgb(255, 255, 255);\n""border-radius: 10px;\n""background-color: rgb(98, 98, 98);")
pushButton.setObjectName("pushButton")
pushButton.clicked.connect(descargar_func)

        
statusbar = QtWidgets.QStatusBar(MainWindow)
statusbar.setObjectName("statusbar")
progressBar.setValue(0)

QtCore.QMetaObject.connectSlotsByName(MainWindow)

def retranslateUi(MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
    titulo_label.setText(_translate("MainWindow", "Youtube Downloader"))
    label_video_url.setText(_translate("MainWindow", "Video URL:"))
    entry_video_url.setPlaceholderText(_translate("MainWindow", "e.j: https://www.youtube.com/watch?v=rfscVS0vtbw"))
    calidad_label.setText(_translate("MainWindow", "Calidad:"))
    comboBox.setCurrentText(_translate("MainWindow", "Mayor calidad Disponible"))
    comboBox.setItemText(0, _translate("MainWindow", "Mayor calidad Disponible"))
    comboBox.setItemText(1, _translate("MainWindow", "1080p"))
    comboBox.setItemText(2, _translate("MainWindow", "720p"))
    comboBox.setItemText(3, _translate("MainWindow", "480p"))
    pushButton.setText(_translate("MainWindow", "Descargar"))

retranslateUi(MainWindow)

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())
