# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mda.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 980)
        MainWindow.setMinimumSize(QtCore.QSize(471, 980))
        MainWindow.setMaximumSize(QtCore.QSize(471, 980))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("QComboBox {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"  \n"
"QComboBox:drop-down {\n"
"    width: 0px;  /* set the width of the drop down */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     background-color: #46465d;\n"
"     width: 15px;\n"
"     margin: 15px 3px 15px 3px;\n"
"     border: 1px transparent #46465d;\n"
"     border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical {\n"
"     background-color: #df6277;         /* #605F5F; */\n"
"     min-height: 5px;\n"
"     border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar:sub-line:vertical {\n"
"     border: None;\n"
"     margin: 3px 0px 3px 0px;      /* # <-------- */\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:add-line:vertical {\n"
"     border: None;\n"
"     margin: 3px 0px 3px 0px;     /* # <-------- */\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar:sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"               /* # <-------- */\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar:add-line:vertical:hover, QScrollBar:add-line:vertical:on {              /* # <-------- */\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:up-arrow:vertical, QScrollBar:down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar:add-page:vertical, QScrollBar:sub-page:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"")
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #303040;\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 471, 91))
        self.frame.setStyleSheet("background-color: #df6277;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 0, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 45, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 110, 481, 851))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
" QTabWidget::pane { /* Рамка виджета со вкладками */\n"
"\n"
"     border-top: 2px solid #df6277;\n"
"     position: absolute;\n"
"     top: -0.8em;\n"
"\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     min-width: 200px;\n"
"     left: 150px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #303040;\n"
"    border: 2px solid #df6277;\n"
"    color: white;\n"
"    border-bottom-color: #df6277; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: #323248;\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.basic = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.basic.setFont(font)
        self.basic.setObjectName("basic")
        self.tikaudio = QtWidgets.QComboBox(self.basic)
        self.tikaudio.setGeometry(QtCore.QRect(180, 575, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tikaudio.setFont(font)
        self.tikaudio.setStyleSheet("")
        self.tikaudio.setObjectName("tikaudio")
        self.formatsvideo = QtWidgets.QPushButton(self.basic)
        self.formatsvideo.setGeometry(QtCore.QRect(180, 240, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.formatsvideo.setFont(font)
        self.formatsvideo.setToolTipDuration(-1)
        self.formatsvideo.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.formatsvideo.setObjectName("formatsvideo")
        self.line_2 = QtWidgets.QFrame(self.basic)
        self.line_2.setGeometry(QtCore.QRect(40, 490, 411, 16))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.basic)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.formatsaudio = QtWidgets.QPushButton(self.basic)
        self.formatsaudio.setGeometry(QtCore.QRect(180, 525, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.formatsaudio.setFont(font)
        self.formatsaudio.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.formatsaudio.setObjectName("formatsaudio")
        self.downloadaudio = QtWidgets.QPushButton(self.basic)
        self.downloadaudio.setGeometry(QtCore.QRect(40, 720, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.downloadaudio.setFont(font)
        self.downloadaudio.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.downloadaudio.setObjectName("downloadaudio")
        self.progress = QtWidgets.QProgressBar(self.basic)
        self.progress.setGeometry(QtCore.QRect(40, 370, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.progress.setFont(font)
        self.progress.setStyleSheet("QProgressBar {\n"
"    border: 2px solid #df6277;\n"
"    color: white;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: #05B8CC;\n"
"     width: 20px;\n"
" }\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid #df6277;\n"
"     text-align: center;\n"
" }")
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.audio = QtWidgets.QRadioButton(self.basic)
        self.audio.setGeometry(QtCore.QRect(40, 535, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.audio.setFont(font)
        self.audio.setStyleSheet("color: white;")
        self.audio.setObjectName("audio")
        self.label_4 = QtWidgets.QLabel(self.basic)
        self.label_4.setGeometry(QtCore.QRect(30, 565, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.url_yout = QtWidgets.QLineEdit(self.basic)
        self.url_yout.setGeometry(QtCore.QRect(40, 80, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.url_yout.setFont(font)
        self.url_yout.setStyleSheet("color: white;\n"
"border: 2px solid #df6277;")
        self.url_yout.setText("")
        self.url_yout.setAlignment(QtCore.Qt.AlignCenter)
        self.url_yout.setObjectName("url_yout")
        self.video = QtWidgets.QRadioButton(self.basic)
        self.video.setGeometry(QtCore.QRect(40, 250, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.video.setFont(font)
        self.video.setStyleSheet("color: white;")
        self.video.setObjectName("video")
        self.line = QtWidgets.QFrame(self.basic)
        self.line.setGeometry(QtCore.QRect(40, 210, 411, 16))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.outfile = QtWidgets.QLineEdit(self.basic)
        self.outfile.setGeometry(QtCore.QRect(40, 150, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.outfile.setFont(font)
        self.outfile.setStyleSheet("color: white;\n"
"border: 2px solid #df6277;")
        self.outfile.setText("")
        self.outfile.setAlignment(QtCore.Qt.AlignCenter)
        self.outfile.setObjectName("outfile")
        self.progress_2 = QtWidgets.QProgressBar(self.basic)
        self.progress_2.setGeometry(QtCore.QRect(40, 665, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.progress_2.setFont(font)
        self.progress_2.setStyleSheet("QProgressBar {\n"
"    border: 2px solid #df6277;\n"
"    color: white;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: #05B8CC;\n"
"     width: 20px;\n"
" }\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid #df6277;\n"
"     text-align: center;\n"
" }")
        self.progress_2.setProperty("value", 0)
        self.progress_2.setObjectName("progress_2")
        self.tikvideo = QtWidgets.QComboBox(self.basic)
        self.tikvideo.setGeometry(QtCore.QRect(180, 290, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tikvideo.setFont(font)
        self.tikvideo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tikvideo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tikvideo.setStyleSheet("")
        self.tikvideo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tikvideo.setEditable(False)
        self.tikvideo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.tikvideo.setFrame(True)
        self.tikvideo.setObjectName("tikvideo")
        self.downloadvideo = QtWidgets.QPushButton(self.basic)
        self.downloadvideo.setGeometry(QtCore.QRect(40, 425, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.downloadvideo.setFont(font)
        self.downloadvideo.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.downloadvideo.setObjectName("downloadvideo")
        self.file = QtWidgets.QPushButton(self.basic)
        self.file.setGeometry(QtCore.QRect(400, 150, 51, 41))
        self.file.setStyleSheet("QPushButton {\n"
"border: None;\n"
"}")
        self.file.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/select_directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file.setIcon(icon)
        self.file.setIconSize(QtCore.QSize(35, 35))
        self.file.setCheckable(False)
        self.file.setObjectName("file")
        self.sbrosdown = QtWidgets.QPushButton(self.basic)
        self.sbrosdown.setGeometry(QtCore.QRect(240, 21, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sbrosdown.setFont(font)
        self.sbrosdown.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.sbrosdown.setObjectName("sbrosdown")
        self.tabWidget.addTab(self.basic, "")
        self.add = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.son1 = QtWidgets.QLineEdit(self.add)
        self.son1.setGeometry(QtCore.QRect(40, 80, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.son1.setFont(font)
        self.son1.setStyleSheet("color: white;\n"
"border: 2px solid #df6277;")
        self.son1.setText("")
        self.son1.setAlignment(QtCore.Qt.AlignCenter)
        self.son1.setObjectName("son1")
        self.son2 = QtWidgets.QLineEdit(self.add)
        self.son2.setGeometry(QtCore.QRect(40, 150, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.son2.setFont(font)
        self.son2.setStyleSheet("color: white;\n"
"border: 2px solid #df6277;")
        self.son2.setText("")
        self.son2.setAlignment(QtCore.Qt.AlignCenter)
        self.son2.setObjectName("son2")
        self.son1_file = QtWidgets.QPushButton(self.add)
        self.son1_file.setGeometry(QtCore.QRect(400, 80, 51, 41))
        self.son1_file.setStyleSheet("QPushButton {\n"
"border: None;\n"
"}")
        self.son1_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/select_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.son1_file.setIcon(icon1)
        self.son1_file.setIconSize(QtCore.QSize(35, 35))
        self.son1_file.setCheckable(False)
        self.son1_file.setObjectName("son1_file")
        self.son2_file = QtWidgets.QPushButton(self.add)
        self.son2_file.setGeometry(QtCore.QRect(400, 150, 51, 41))
        self.son2_file.setStyleSheet("QPushButton {\n"
"border: None;\n"
"}")
        self.son2_file.setText("")
        self.son2_file.setIcon(icon1)
        self.son2_file.setIconSize(QtCore.QSize(35, 35))
        self.son2_file.setCheckable(False)
        self.son2_file.setObjectName("son2_file")
        self.skvideoandaudio = QtWidgets.QPushButton(self.add)
        self.skvideoandaudio.setGeometry(QtCore.QRect(40, 290, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.skvideoandaudio.setFont(font)
        self.skvideoandaudio.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.skvideoandaudio.setObjectName("skvideoandaudio")
        self.son3_file = QtWidgets.QPushButton(self.add)
        self.son3_file.setGeometry(QtCore.QRect(400, 220, 51, 41))
        self.son3_file.setStyleSheet("QPushButton {\n"
"border: None;\n"
"}")
        self.son3_file.setText("")
        self.son3_file.setIcon(icon)
        self.son3_file.setIconSize(QtCore.QSize(35, 35))
        self.son3_file.setCheckable(False)
        self.son3_file.setObjectName("son3_file")
        self.son3 = QtWidgets.QLineEdit(self.add)
        self.son3.setGeometry(QtCore.QRect(40, 220, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.son3.setFont(font)
        self.son3.setStyleSheet("color: white;\n"
"border: 2px solid #df6277;")
        self.son3.setText("")
        self.son3.setAlignment(QtCore.Qt.AlignCenter)
        self.son3.setObjectName("son3")
        self.sbrosskl = QtWidgets.QPushButton(self.add)
        self.sbrosskl.setGeometry(QtCore.QRect(240, 21, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sbrosskl.setFont(font)
        self.sbrosskl.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.sbrosskl.setObjectName("sbrosskl")
        self.tabWidget.addTab(self.add, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.menu.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/menu_programm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon2)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.developer = QtWidgets.QAction(MainWindow)
        self.developer.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images/internet_developer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.developer.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.developer.setFont(font)
        self.developer.setObjectName("developer")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/images/instruction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.menu.addAction(self.help)
        self.menu.addAction(self.developer)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quantum Downloader"))
        self.label_2.setText(_translate("MainWindow", "V.0.1.B Free"))
        self.tikaudio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Поле, где можно выбрать один из вариантов для загрузки аудиофайла </p></body></html>"))
        self.formatsvideo.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка, чтобы узнать данные об доступных вариантах для загрузки видеофайла</p></body></html>"))
        self.formatsvideo.setText(_translate("MainWindow", "УЗНАТЬ ФОРМАТЫ"))
        self.label_3.setText(_translate("MainWindow", "ФОРМАТЫ"))
        self.formatsaudio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка, чтобы узнать данные об доступных вариантах для загрузки аудиофайла</p></body></html>"))
        self.formatsaudio.setText(_translate("MainWindow", "УЗНАТЬ ФОРМАТЫ"))
        self.downloadaudio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для загрузки аудиофайла</p></body></html>"))
        self.downloadaudio.setText(_translate("MainWindow", "СКАЧАТЬ АУДИО"))
        self.progress.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Строка прогресса загрузки видеофайла</p></body></html>"))
        self.audio.setText(_translate("MainWindow", "АУДИО"))
        self.label_4.setText(_translate("MainWindow", "ФОРМАТЫ"))
        self.url_yout.setPlaceholderText(_translate("MainWindow", "Введите URL с YouTube"))
        self.video.setText(_translate("MainWindow", "ВИДЕО"))
        self.outfile.setPlaceholderText(_translate("MainWindow", "Выберите директорию"))
        self.progress_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Строка прогресса загрузки аудиофайла</p></body></html>"))
        self.tikvideo.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Поле, где можно выбрать один из вариантов для загрузки видеофайла </p></body></html>"))
        self.downloadvideo.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для загрузки видеофайла</p></body></html>"))
        self.downloadvideo.setText(_translate("MainWindow", "СКАЧАТЬ ВИДЕО"))
        self.file.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для указания директории</p></body></html>"))
        self.sbrosdown.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для сброса всех данных во вкладке &quot;Скачать&quot;</p></body></html>"))
        self.sbrosdown.setText(_translate("MainWindow", "СБРОСИТЬ ВСЁ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basic), _translate("MainWindow", "Скачать"))
        self.son1.setPlaceholderText(_translate("MainWindow", "Выберите видео файл"))
        self.son2.setPlaceholderText(_translate("MainWindow", "Выберите аудио файл"))
        self.son1_file.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопк для указания видеофайла</p></body></html>"))
        self.son2_file.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для указания аудиофайла</p></body></html>"))
        self.skvideoandaudio.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для склеивания видеофайла и аудиофайла</p></body></html>"))
        self.skvideoandaudio.setText(_translate("MainWindow", "СКЛЕИТЬ"))
        self.son3_file.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для указания имени и директории выходного видеофайла</p></body></html>"))
        self.son3.setPlaceholderText(_translate("MainWindow", "Выберите директорию"))
        self.sbrosskl.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Кнопка для сброса всех данных во вкладке &quot;Склеить&quot;</p></body></html>"))
        self.sbrosskl.setText(_translate("MainWindow", "СБРОСИТЬ ВСЁ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("MainWindow", "Склеить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.developer.setText(_translate("MainWindow", "Связь с разработчиком"))
        self.developer.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.help.setText(_translate("MainWindow", "Помощь"))
        self.help.setShortcut(_translate("MainWindow", "Ctrl+Q"))
import icons_ha_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
