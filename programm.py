from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressBar, QComboBox
from PyQt5.QtCore import QThread, pyqtSignal, QWaitCondition, QMutex
from pytube import YouTube
from mda import Ui_MainWindow
import os
import os.path
import sys
import urllib.request 
import ctypes
import validators
import webbrowser
import time
import urllib.request
import pafy
import subprocess

global url_yout
global outfile
global audio_file_2
global video_file_2
global tikvideo


class MainApp(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainApp, self).__init__()
        self.mda = Ui_MainWindow()
        self.mda.setupUi(self)
        self.window_settings()

        self.mda.son1.setReadOnly(True)
        self.mda.son2.setReadOnly(True)
        self.mda.son3.setReadOnly(True)
        self.mda.outfile.setReadOnly(True)

        self.mda.help.triggered.connect(self.help_command)
        self.mda.son1_file.clicked.connect(self.video_open)
        self.mda.son2_file.clicked.connect(self.audio_open)

        self.mda.sbrosskl.clicked.connect(self.sbrosskleyka)
        self.mda.sbrosdown.clicked.connect(self.sbrosall)
        
        self.mda.son3_file.clicked.connect(self.select_out_directory_file)

        self.mda.skvideoandaudio.clicked.connect(self.skleyka)

        self.mda.formatsvideo.clicked.connect(self.video_settings)
        self.mda.downloadvideo.clicked.connect(self.check)
        self.mda.file.clicked.connect(self.select_directory)
        self.mda.video.setAutoExclusive(False)

        self.mda.formatsaudio.clicked.connect(self.audio_settings)
        self.mda.audio.setAutoExclusive(False)
        self.mda.downloadaudio.clicked.connect(self.check2)
        self.mda.developer.triggered.connect(lambda: webbrowser.open('https://t.me/dav1d_sv1d'))

    def window_settings(self):

    
        
        self.setWindowTitle("Quantum Downloader V.0.1.B Free")

        self.setWindowIcon(QIcon("D:\Davids_pack\Скачиватель\images\programm_icon"))



    # --------------------СКАЧИВАНИЕ ОДНОГО ВИДЕО--------------------

    # ПРИ НАЖАТИИ НА "УЗНАТЬ ФОРМАТЫ" ИДЁТ ПРОВЕРКА НА ПРАВИЛЬНОСТЬ URL И КОРРЕКТНОГО ПУТИ, ЕСЛИ ВСЁ ХОРОШО, ДЕЛАЕМ НАСТРОЙКИ ДЛЯ ВИДЕО-ФОРМАТОВ
    def video_settings(self):

        url_yout = str(self.mda.url_yout.text())
        outfile = str(self.mda.outfile.text())


        if url_yout == '' and outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL, а так же, выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)

        elif url_yout == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL", u"", MB_OK | ICON_EXLAIM, 0)

        elif not validators.url(url_yout):
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный URL", u"Ошибка некорректного URL", MB_OK | ICON_STOP, 0)

        elif outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)


        elif os.path.exists(outfile) == False:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная директория", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)

        elif self.mda.video.isChecked() and self.mda.audio.isChecked():

            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Должен быть выбран только один пункт", u"Ошибка выбора двух пунктов", MB_OK | ICON_STOP, 0)

            self.mda.video.setCheckable(False)
            self.mda.video.setCheckable(True)
            self.mda.video.setAutoExclusive(False)
            self.mda.tikvideo.clear()

            self.mda.audio.setCheckable(False)
            self.mda.audio.setCheckable(True)
            self.mda.audio.setAutoExclusive(False)
            self.mda.tikaudio.clear()



        else:
            global video_streams
            

            if self.mda.video.isChecked():

                if 'youtube.com/' in url_yout or 'https://www.youtube.com/' in url_yout or 'youtu.be/' in url_yout or 'https://www.youtu.be/'
                    if 'https://www.youtube.com/playlist?list' in url_yout or 'youtube.com/playlist?list' in url_yout:
                        MB_OK = 0x0
                        MB_OKCXL = 0x01
                        MB_YESNOCXL = 0x03
                        MB_YESNO = 0x04
                        MB_HELP = 0x4000
                        ICON_EXLAIM = 0x30
                        ICON_INFO = 0x40
                        ICON_STOP = 0x10
                        MB_CANCELTRYCONTINUE = 0x2

                        self.result = ctypes.windll.user32.MessageBoxW(0, u"Невозможно скачать видеофайл с плейлиста", u"", MB_OK | ICON_EXLAIM, 0)

                    elif "list" in url_yout:
                        MB_OK = 0x0
                        MB_OKCXL = 0x01
                        MB_YESNOCXL = 0x03
                        MB_YESNO = 0x04
                        MB_HELP = 0x4000
                        ICON_EXLAIM = 0x30
                        ICON_INFO = 0x40
                        ICON_STOP = 0x10
                        MB_CANCELTRYCONTINUE = 0x2

                        self.result = ctypes.windll.user32.MessageBoxW(0, u"Невозможно скачать видеофайл с плейлиста", u"", MB_OK | ICON_EXLAIM, 0)

                    else:
                    
                        video = pafy.new(url_yout)
                        video_streams = video.videostreams
                            
                        mda = ' | ' 
                        mda2 = ' | '


                        for stream in video_streams:
                            size = stream.get_filesize()
                            data = "{} {mda} {} {mda2} {}".format(stream.extension, stream.quality, size, mda = mda, mda2 = mda2)
                                        
                            self.mda.tikvideo.addItem(data)
                else:
                    MB_OK = 0x0
                    MB_OKCXL = 0x01
                    MB_YESNOCXL = 0x03
                    MB_YESNO = 0x04
                    MB_HELP = 0x4000
                    ICON_EXLAIM = 0x30
                    ICON_INFO = 0x40
                    ICON_STOP = 0x10
                    MB_CANCELTRYCONTINUE = 0x2

                    self.result = ctypes.windll.user32.MessageBoxW(0, u"URL с других сайтов кроме YouTube запрещены", u"", MB_OK | ICON_EXLAIM, 0)

            else:

                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите пункт для скачивания", u"", MB_OK | ICON_EXLAIM, 0)



    # ПРОВЕРКА НА ПРАВИЛЬНО ВЫБРАННЫЙ ПУТЬ, ЕСЛИ ВСЁ ХОРОШО, ПУТЬ ПИШЕТСЯ
    def select_directory(self):


        folder = QFileDialog.getExistingDirectory(self, "Выберите директорию")
        if folder == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)

        elif os.path.exists(folder):
            self.mda.outfile.setText(folder)
        else:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная директория", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)




    # ПРИ НАЖАТИИ НА КНОПКУ "СКАЧАТЬ" ЕЩЁ РАЗ ИДЁТ ПРОВЕРКА НА ПРАВИЛЬНО URL И КОРРЕКТНОГО ПУТИ, ЕСЛИ ВСЁ ХОРОШО, СКАЧИВАЕМ И ВЫЗЫВАЕМ СТРОКУ ПРОГРЕССА
    def check(self):

        url_yout = str(self.mda.url_yout.text())
        outfile = str(self.mda.outfile.text())
        tikvideo = str(self.mda.tikvideo.currentText())

        if url_yout == '' and outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL, а так же, выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)


        elif url_yout == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL", u"", MB_OK | ICON_EXLAIM, 0)

        elif not validators.url(url_yout):
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный URL", u"Ошибка некорректного URL", MB_OK | ICON_STOP, 0)

        elif outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)


        elif os.path.exists(outfile) == False:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная директория", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)

        elif tikvideo == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Не выбран вариант для скачивания", u"", MB_OK | ICON_STOP, 0)


        else:
            video_quality = self.mda.tikvideo.currentIndex()
            download = video_streams[video_quality].download(filepath = outfile, callback = self.Video_Progress)
            
    def Video_Progress(self, total, received, ratio, rate, time):

        read_data = received
        if total > 0 :
            download_percentage = read_data * 100 / total
            self.mda.progress.setValue(download_percentage)
            QApplication.processEvents()

            if download_percentage == 100:
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Загрузка завершена", u"", MB_OK | ICON_INFO, 0)
                self.mda.url_yout.setText('')
                self.mda.outfile.setText('')
                self.mda.video.setCheckable(False)
                self.mda.video.setCheckable(True)
                self.mda.video.setAutoExclusive(False)
                self.mda.progress.setValue(0)
                self.mda.tikvideo.clear()

    # --------------------СКАЧИВАНИЕ ОДНОГО АУДИО--------------------

    # ПРИ НАЖАТИИ НА "УЗНАТЬ ФОРМАТЫ" ИДЁТ ПРОВЕРКА НА ПРАВИЛЬНОСТЬ URL И КОРРЕКТНОГО ПУТИ, ЕСЛИ ВСЁ ХОРОШО, ДЕЛАЕМ НАСТРОЙКИ ДЛЯ АУДИО-ФОРМАТОВ         
    def audio_settings(self):

        url_yout = str(self.mda.url_yout.text())
        outfile = str(self.mda.outfile.text())

        if url_yout == '' and outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL, а так же, выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)

        elif url_yout == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL", u"", MB_OK | ICON_EXLAIM, 0)

        elif not validators.url(url_yout):
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный URL", u"Ошибка некорректного URL", MB_OK | ICON_STOP, 0)

        elif outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)

        elif os.path.exists(outfile) == False:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)

        elif self.mda.video.isChecked() and self.mda.audio.isChecked():
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Должен быть выбран только один пункт для скачивания", u"", MB_OK | ICON_STOP, 0)

            self.mda.video.setCheckable(False)
            self.mda.video.setCheckable(True)
            self.mda.video.setAutoExclusive(False)
            self.mda.tikvideo.clear()
            

            self.mda.audio.setCheckable(False)
            self.mda.audio.setCheckable(True)
            self.mda.audio.setAutoExclusive(False)
            self.mda.tikaudio.clear()
        
        else:

            if self.mda.audio.isChecked():

                if 'youtube.com/' in url_yout or 'https://www.youtube.com/' in url_yout:
                    if 'https://www.youtube.com/playlist?list' in url_yout or 'youtube.com/playlist?list' in url_yout:
                        MB_OK = 0x0
                        MB_OKCXL = 0x01
                        MB_YESNOCXL = 0x03
                        MB_YESNO = 0x04
                        MB_HELP = 0x4000
                        ICON_EXLAIM = 0x30
                        ICON_INFO = 0x40
                        ICON_STOP = 0x10
                        MB_CANCELTRYCONTINUE = 0x2

                        self.result = ctypes.windll.user32.MessageBoxW(0, u"Невозможно скачать видеофайл с плейлиста", u"", MB_OK | ICON_EXLAIM, 0)

                    elif "list" in url_yout:
                        MB_OK = 0x0
                        MB_OKCXL = 0x01
                        MB_YESNOCXL = 0x03
                        MB_YESNO = 0x04
                        MB_HELP = 0x4000
                        ICON_EXLAIM = 0x30
                        ICON_INFO = 0x40
                        ICON_STOP = 0x10
                        MB_CANCELTRYCONTINUE = 0x2

                        self.result = ctypes.windll.user32.MessageBoxW(0, u"Невозможно скачать видеофайл с плейлиста", u"", MB_OK | ICON_EXLAIM, 0)

                    else:

                        audio = pafy.new(url_yout)
                        audio_streams = audio.audiostreams

                        mda3 = ' | '
                        mda4 = ' | '

                        for stream in audio_streams:
                            size = stream.get_filesize()
                            data = "{} {mda3} {} {mda4} {}".format(stream.bitrate, stream.extension, size, mda3 = mda3, mda4 = mda4)
                            self.mda.tikaudio.addItem(data)
                            
                else:
                    MB_OK = 0x0
                    MB_OKCXL = 0x01
                    MB_YESNOCXL = 0x03
                    MB_YESNO = 0x04
                    MB_HELP = 0x4000
                    ICON_EXLAIM = 0x30
                    ICON_INFO = 0x40
                    ICON_STOP = 0x10
                    MB_CANCELTRYCONTINUE = 0x2

                    self.result = ctypes.windll.user32.MessageBoxW(0, u"URL с других сайтов кроме YouTube запрещены", u"", MB_OK | ICON_EXLAIM, 0)

            else:

                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите пункт для скачивания", u"", MB_OK | ICON_EXLAIM, 0)

    # ПРИ НАЖАТИИ НА КНОПКУ "СКАЧАТЬ" ЕЩЁ РАЗ ИДЁТ ПРОВЕРКА НА ПРАВИЛЬНО URL И КОРРЕКТНОГО ПУТИ, ЕСЛИ ВСЁ ХОРОШО, СКАЧИВАЕМ И ВЫЗЫВАЕМ СТРОКУ ПРОГРЕССА
    def check2(self):

        url_yout = str(self.mda.url_yout.text())
        outfile = str(self.mda.outfile.text())
        tikaudio = str(self.mda.tikaudio.currentText())

        if url_yout == '' and outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL, а так же, выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)


        elif url_yout == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Введите URL", u"", MB_OK | ICON_EXLAIM, 0)

        elif not validators.url(url_yout):
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный URL", u"Ошибка некорректного URL", MB_OK | ICON_STOP, 0)

        elif outfile == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию", u"", MB_OK | ICON_EXLAIM, 0)


        elif os.path.exists(outfile) == False:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная директория", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)

        elif tikaudio == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Не выбран вариант для скачивания", u"", MB_OK | ICON_STOP, 0)


        else:
            audio = pafy.new(url_yout)
            audio_stream = audio.audiostreams
            audio_bitrate = self.mda.tikvideo.currentIndex()
            download2 = audio_stream[audio_bitrate].download(filepath = outfile, callback = self.Audio_Progress)

    def Audio_Progress(self, total, received, ratio, rate, time):

        read_data = received
        if total > 0 :
            download_percentage = read_data * 100 / total
            self.mda.progress_2.setValue(download_percentage)
            QApplication.processEvents()

            if download_percentage == 100:
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Загрузка завершена", u"", MB_OK | ICON_INFO, 0)
                self.mda.url_yout.setText('')
                self.mda.outfile.setText('')
                self.mda.audio.setCheckable(False)
                self.mda.audio.setCheckable(True)
                self.mda.audio.setAutoExclusive(False)
                self.mda.progress_2.setValue(0)
                self.mda.tikaudio.clear()

    def help_command(self):
        MB_OK = 0x0
        MB_OKCXL = 0x01
        MB_YESNOCXL = 0x03
        MB_YESNO = 0x04
        MB_HELP = 0x4000
        ICON_EXLAIM = 0x30
        ICON_INFO = 0x40
        ICON_STOP = 0x10
        MB_CANCELTRYCONTINUE = 0x2

        self.result = ctypes.windll.user32.MessageBoxW(0, u'''           Здравствуйте пользователи этой программы!

            ▼ Сразу перейду к инструкциям вкладок ▼

                            ✸ Вкладка "Скачать"

Во вкладке "Скачать" вы можете
скачать либо аудиофайл либо видеофайл (без звука).

▼ Инструкция по скачке ▼

➜ В первом поле вы вводите\nURL ссылку с YouTube.
            \n➜ Во втором поле вы нажимаете
на значок, и выбираете директорию.

➜ Затем вы выбираете или пункт
"ВИДЕО" или пункт "АУДИО", и нажимаете
"УЗНАТЬ ФОРМАТЫ". После нажатия
вы можете выбрать один из вариантов
для скачивания.
            \n➜ Далее выбираете кнопку для
скачивания основываясь на том,
какую галочку вы выбрали.

Если вы желаете сбросить всё что выбрали,
нажмите на кнопку "СБРОСИТЬ ВСЁ".

                            ✸ Вкладка "Склеить"

Во складке "Склеить" вы можете
склеить видеофайл и аудиофайл в один видеофайл.

▼ Инструкция по склеиванию ▼

➜ В первом поле вы нажимаете на значок
и выбираете видеофайл.

➜ Во втором поле вы нажимаете на значок
и выбираете аудиофайл.

➜ В третьем поле вы нажимаете на значок
и выбираете директорию для сохранения выходного
файла, а так же, вводите имя выходному файлу.

➜ Далее просто нажимаете на кнопку "Склеить".

Если вы желаете сбросить всё что выбрали,
нажмите на кнопку "СБРОСИТЬ ВСЁ".

            
            \nУдачного использования программы!'''
        , u"Помощь в использовании программы", MB_OK | ICON_INFO, 0)

    def video_open(self):
        global video_file_2

        video_file_2 = QFileDialog.getOpenFileName(self, 'Выберите видеофайл', '')[0]
        if video_file_2 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите видеофайл", u"", MB_OK | ICON_EXLAIM, 0)

        elif os.path.exists(video_file_2):
            if '/' in video_file_2:
                video_name_2 = video_file_2.split('/')
                video_name_video = video_name_2[-1]
                self.mda.son1.setText(video_name_video)
            else:
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите видеофайл", u"", MB_OK | ICON_EXLAIM, 0)
        else:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный видеофайл", u"Ошибка некорректного видеофайла", MB_OK | ICON_STOP, 0)

    def audio_open(self):
        global audio_file_2

        audio_file_2 = QFileDialog.getOpenFileName(self, 'Выберите аудиофайл', '')[0]
        if audio_file_2 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите аудиофайл", u"", MB_OK | ICON_EXLAIM, 0)

        elif os.path.exists(audio_file_2):
            if '/' in audio_file_2:
                audio_name_2 = audio_file_2.split('/')
                audio_name_audio = audio_name_2[-1]
                self.mda.son2.setText(audio_name_audio)
            else:
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите аудиофайл", u"", MB_OK | ICON_EXLAIM, 0)
        else:
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректный аудиофайл", u"Ошибка некорректного аудиофайла", MB_OK | ICON_STOP, 0)

    def select_out_directory_file(self):
        
        global file_folder

        file_folder = QFileDialog.getSaveFileName(self, "Выберите директорию и введите имя файла", '/', 'MP4 файлы - *.mp4, MKV файлы - *.mkv, AVI файлы - *.avi')[0]

        if os.path.exists(file_folder):
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Некорректная директория", u"Ошибка некорректной директории", MB_OK | ICON_STOP, 0)

        elif file_folder == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию и введите имя файла", u"", MB_OK | ICON_EXLAIM, 0)

        self.mda.son3.setText(file_folder)

    def skleyka(self):

        son1 = str(self.mda.son1.text())
        son2 = str(self.mda.son2.text())
        son3 = str(self.mda.son3.text())

        if son1 == '' and son2 == '' and son3 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите видеофайл, аудиофайл, а так же выберите директорию и имя выходного файла", u"", MB_OK | ICON_EXLAIM, 0)

        elif son1 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите видеофайл", u"", MB_OK | ICON_EXLAIM, 0)
        
        elif son2 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите аудиофайл", u"", MB_OK | ICON_EXLAIM, 0)

        elif son3 == '':
            MB_OK = 0x0
            MB_OKCXL = 0x01
            MB_YESNOCXL = 0x03
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_EXLAIM = 0x30
            ICON_INFO = 0x40
            ICON_STOP = 0x10
            MB_CANCELTRYCONTINUE = 0x2

            self.result = ctypes.windll.user32.MessageBoxW(0, u"Выберите директорию и имя выходного файла", u"", MB_OK | ICON_INFO, 0)

        else:
           
            if '.webm' in video_file_2[-5:] and '.m4a' in audio_file_2[-4:] or '.mp3' in audio_file_2[-4:]: 
                cmd = '"ffmpeg" "-i" "{}" "-i" "{}" "-c" "copy" "-shortest" "{}"'.format(video_file_2, audio_file_2, file_folder)
                subprocess.call(cmd, shell=True)
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Склеивание завершено", u"", MB_OK | ICON_INFO, 0)
                self.mda.son1.setText('')
                self.mda.son2.setText('')
                self.mda.son3.setText('')

            elif '.mp4' in video_file_2[-4:] and '.m4a' in audio_file_2[-4:] or '.mp3' in audio_file_2[-4:]: 
                cmd = '"ffmpeg" "-i" "{}" "-i" "{}" "-c" "copy" "-shortest" "{}"'.format(video_file_2, audio_file_2, file_folder)
                subprocess.call(cmd, shell=True)
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u"Склеивание завершено", u"", MB_OK | ICON_INFO, 0)
                self.mda.son1.setText('')
                self.mda.son2.setText('')
                self.mda.son3.setText('')
                       
            else:
                MB_OK = 0x0
                MB_OKCXL = 0x01
                MB_YESNOCXL = 0x03
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_EXLAIM = 0x30
                ICON_INFO = 0x40
                ICON_STOP = 0x10
                MB_CANCELTRYCONTINUE = 0x2

                self.result = ctypes.windll.user32.MessageBoxW(0, u'''Программа может склеивать только такие форматы:

Видео: .webm, .mp4
Аудио: .m4a, .mp3

Например: .webm + .m4a, .webm + .mp3, .mp4 + .m4a, .mp4 + .mp3 ''', u"", MB_OK | ICON_EXLAIM, 0)

    def sbrosskleyka(self):
        self.mda.son1.setText('')
        self.mda.son2.setText('')
        self.mda.son3.setText('')

    def sbrosall(self):
        self.mda.url_yout.setText('')
        self.mda.outfile.setText('')

        self.mda.video.setCheckable(False)
        self.mda.video.setCheckable(True)
        self.mda.video.setAutoExclusive(False)
        self.mda.progress.setValue(0)
        self.mda.tikvideo.clear()

        self.mda.audio.setCheckable(False)
        self.mda.audio.setCheckable(True)
        self.mda.audio.setAutoExclusive(False)
        self.mda.progress_2.setValue(0)
        self.mda.tikaudio.clear()

app = QtWidgets.QApplication([])
aplication = MainApp()
aplication.show()

sys.exit(app.exec_())
