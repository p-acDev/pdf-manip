# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_pdf_manipulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 690)
        MainWindow.setMinimumSize(QtCore.QSize(570, 690))
        MainWindow.setMaximumSize(QtCore.QSize(570, 690))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 100, 501, 438))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget_filenames = QtWidgets.QTreeWidget(self.gridLayoutWidget)
        self.treeWidget_filenames.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget_filenames.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget_filenames.setAlternatingRowColors(True)
        self.treeWidget_filenames.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget_filenames.setObjectName("treeWidget_filenames")
        self.gridLayout.addWidget(self.treeWidget_filenames, 3, 0, 1, 1)
        self.pushButton_browse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_browse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout.addWidget(self.pushButton_browse, 7, 0, 1, 1)
        self.pushButton_preview = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_preview.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.gridLayout.addWidget(self.pushButton_preview, 10, 0, 1, 1)
        self.pushButton_merge = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_merge.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_merge.setObjectName("pushButton_merge")
        self.gridLayout.addWidget(self.pushButton_merge, 9, 0, 1, 1)
        self.pushButton_removeFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_removeFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_removeFile.setObjectName("pushButton_removeFile")
        self.gridLayout.addWidget(self.pushButton_removeFile, 3, 1, 1, 1)
        self.pushButton_removePages = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_removePages.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_removePages.setObjectName("pushButton_removePages")
        self.gridLayout.addWidget(self.pushButton_removePages, 11, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Josefin Sans SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(410, 610, 72, 30))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 550, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(65, 583, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Josefin Sans SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_version.setFont(font)
        self.label_version.setObjectName("label_version")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(65, 618, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Josefin Sans SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_author.setFont(font)
        self.label_author.setObjectName("label_author")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 594, 20, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_filenames.headerItem().setText(0, _translate("MainWindow", "Item"))
        self.treeWidget_filenames.headerItem().setText(1, _translate("MainWindow", "Directory"))
        self.treeWidget_filenames.headerItem().setText(2, _translate("MainWindow", "file"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_preview.setText(_translate("MainWindow", "Preview"))
        self.pushButton_merge.setText(_translate("MainWindow", "Merge"))
        self.pushButton_removeFile.setText(_translate("MainWindow", "remove"))
        self.pushButton_removePages.setText(_translate("MainWindow", "Remove Page(s)"))
        self.label.setText(_translate("MainWindow", "PDF manipulator"))
        self.label_version.setText(_translate("MainWindow", "version"))
        self.label_author.setText(_translate("MainWindow", "author: p-a.c"))
